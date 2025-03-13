import os
import tempfile
import PyPDF2
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from sentence_transformers import SentenceTransformer
from pymilvus import (
    connections,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
    utility,
)
import logging
import requests

# 配置日志
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# 初始化 FastAPI 应用
app = FastAPI()


# 连接到 Milvus
def connect_to_milvus():
    try:
        connections.connect(alias="default", host="localhost", port="19530")
        # connections.connect(
        #     host="c-e4cd9122cafde16e.milvus.aliyuncs.com",
        #     user="root",
        #     password="Root@123",
        #     port="19530",
        # )
        return True
    except Exception as e:
        logging.error(f"Failed to connect to Milvus: {e}")
        return False


# 创建 Milvus 集合
def create_milvus_collection():
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=2000),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
    ]
    schema = CollectionSchema(fields=fields, description="Knowledge Base Collection")
    collection_name = "knowledge_base123"
    if not utility.has_collection(collection_name):
        collection = Collection(name=collection_name, schema=schema)
        index = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 128},
        }
        collection.create_index(field_name="embedding", index_params=index)
        logging.info(f"Created Milvus collection: {collection_name}")
    else:
        collection = Collection(name=collection_name)
        logging.info(f"Retrieved existing Milvus collection: {collection_name}")
    collection.load()
    return collection


# 分割 PDF 文本
def split_pdf_text(pdf_path):
    text_chunks = []
    try:
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text = page.extract_text()
                chunks = text.split("\n\n")
                text_chunks.extend([chunk.strip() for chunk in chunks if chunk.strip()])
        return text_chunks
    except Exception as e:
        logging.error(f"Error splitting PDF text: {e}")
        return []


# 文本向量化
def vectorize_text(text_chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(text_chunks)
    return embeddings


# 将向量化数据存储到 Milvus
def save_to_milvus(collection, text_chunks, embeddings):
    data = [text_chunks, embeddings.tolist()]
    try:
        collection.insert(data)
        collection.flush()
        logging.info("Data inserted into Milvus successfully.")
    except Exception as e:
        logging.error(f"Failed to insert data into Milvus: {e}")
        raise


# 搜索知识库
def search_knowledge_base(collection, query, top_k=5):
    try:
        model = SentenceTransformer("all-MiniLM-L6-v2")
        query_embedding = model.encode([query])
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        results = collection.search(
            data=query_embedding,
            anns_field="embedding",
            param=search_params,
            limit=top_k,
            output_fields=["text"],
        )
        hits = []
        for hit in results[0]:
            hits.append({"text": hit.entity.get("text"), "distance": hit.distance})
        return hits
    except Exception as e:
        logging.error(f"Error searching in Milvus: {e}")
        raise


# 提供 HTML 页面
@app.get("/")
def get_index():
    return FileResponse("知识库搭建/knowledge.html")


# 处理 PDF 文件上传
@app.post("/upload_pdf")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    if not connect_to_milvus():
        raise HTTPException(status_code=500, detail="Failed to connect to Milvus.")
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            contents = await pdf_file.read()
            temp.write(contents)
            temp_path = temp.name
        text_chunks = split_pdf_text(temp_path)
        if not text_chunks:
            os.remove(temp_path)
            raise HTTPException(
                status_code=400, detail="No valid text extracted from the PDF."
            )
        embeddings = vectorize_text(text_chunks)
        collection = create_milvus_collection()
        save_to_milvus(collection, text_chunks, embeddings)
        os.remove(temp_path)
        return {"message": "PDF processed and data saved to Milvus successfully."}
    except Exception as e:
        logging.error(f"Error processing PDF: {e}")
        raise HTTPException(
            status_code=500, detail=f"An error occurred during PDF processing: {str(e)}"
        )


# 搜索接口
@app.get("/search")
async def search(query: str):
    if not connect_to_milvus():
        raise HTTPException(status_code=500, detail="Failed to connect to Milvus.")
    try:
        collection = create_milvus_collection()
        results = search_knowledge_base(collection, query)
        print(results)
        # 调用本地 deepseek 聊天模型
        chat_url = "http://localhost:11434/api/chat"
        chat_data = {
            "model": "deepseek-r1:14b",
            "messages": [
                {"role": "system", "content": results[0]["text"]},
                {"role": "user", "content": query},
            ],
            "stream": False,
            # "format": "json"  # 指定输出格式为 JSON
        }
        chat_response = requests.post(chat_url, json=chat_data)

        print(chat_response.text)
        # 返回聊天模型的结果
        return {"results": chat_response.text}
    except Exception as e:
        logging.error(f"Error during search: {e}")
        raise HTTPException(
            status_code=500, detail=f"An error occurred during search: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
