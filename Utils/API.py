import os
import PyPDF2
import logging
from sentence_transformers import SentenceTransformer
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from fastapi import FastAPI, HTTPException
import uvicorn

# 配置日志记录
logging.basicConfig(level=logging.ERROR)

# 连接到 Milvus
def connect_to_milvus():
    try:
        connections.connect(
            alias="default",
            host='localhost',
            port='19530'
        )
        return True
    except Exception as e:
        logging.error(f"Failed to connect to Milvus: {e}")
        return False

# 创建 Milvus 集合，增大 text 字段的最大长度
def create_milvus_collection():
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=2000),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384)
    ]
    schema = CollectionSchema(fields=fields, description="PDF Text Embeddings")
    if not utility.has_collection("pdf_text_embeddings2"):
        try:
            collection = Collection(name="pdf_text_embeddings2", schema=schema)
            logging.info("Created Milvus collection: pdf_text_embeddings2")
            return collection
        except Exception as e:
            logging.error(f"Failed to create Milvus collection: {e}")
            raise
    else:
        collection = Collection(name="pdf_text_embeddings2")
        logging.info("Retrieved existing Milvus collection: pdf_text_embeddings2")
        return collection

# 分割 PDF 文本
def split_pdf_text(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The PDF file {pdf_path} does not exist.")
    text_chunks = []
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text = page.extract_text()
                chunks = text.split('\n\n')
                text_chunks.extend([chunk.strip() for chunk in chunks if chunk.strip()])
        return text_chunks
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        return []

# 文本向量化
def vectorize_text(text_chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(text_chunks)
    return embeddings

# 截断文本
def truncate_text(text, max_length):
    return text[:max_length]

# 将向量化数据存储到 Milvus，并创建索引
def save_to_milvus(collection, text_chunks, embeddings):
    truncated_text_chunks = [truncate_text(text, 2000) for text in text_chunks]
    data = [
        truncated_text_chunks,
        embeddings
    ]
    try:
        collection.insert(data)
        collection.flush()
        logging.info("Data inserted into Milvus successfully.")

        # 创建索引
        index = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 128}
        }
        collection.create_index(field_name="embedding", index_params=index)
        logging.info("Index created for the collection.")
    except Exception as e:
        logging.error(f"Failed to insert data or create index in Milvus: {e}")
        raise

# 搜索知识库
def search_knowledge_base(collection, query, top_k=5):
    try:
        # 加载集合到内存
        collection.load()
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_embedding = model.encode([query])
        print(query)
        print(query_embedding)
        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10}
        }
        results = collection.search(
            data=query_embedding,
            anns_field="embedding",
            param=search_params,
            limit=top_k,
            output_fields=["text"]
        )
        hits = []
        for hit in results[0]:
            hits.append({
                "text": hit.entity.get('text'),
                "distance": hit.distance
            })
            print(hit.entity.get('text'))
            print(hit.distance)
        # 释放集合内存（可选，根据实际情况决定是否释放）
        collection.release()
        return hits
    except Exception as e:
        logging.error(f"Error during search in Milvus: {e}")
        raise

# 创建 FastAPI 应用
app = FastAPI()

@app.get("/process_pdf")
async def process_pdf(pdf_path: str):
    if not connect_to_milvus():
        raise HTTPException(status_code=500, detail="Failed to connect to Milvus.")
    try:
        text_chunks = split_pdf_text(pdf_path)
        if not text_chunks:
            raise HTTPException(status_code=400, detail="No valid text extracted from the PDF.")
        embeddings = vectorize_text(text_chunks)
        print("向量化------" + str(embeddings))
        collection = create_milvus_collection()        

        save_to_milvus(collection, text_chunks, embeddings)
        return {"message": "PDF processed and data saved to Milvus successfully."}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"The PDF file {pdf_path} was not found.")
    except Exception as e:
        logging.error(f"Error in /process_pdf: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An error occurred during processing: {str(e)}")

@app.get("/search")
async def search(query: str):
    if not connect_to_milvus():
        raise HTTPException(status_code=500, detail="Failed to connect to Milvus.")
    try:
        collection = create_milvus_collection()
        results = search_knowledge_base(collection, query)
        print(results)
        return {"results": results}
    except Exception as e:
        logging.error(f"Error in /search: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An error occurred during search: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)