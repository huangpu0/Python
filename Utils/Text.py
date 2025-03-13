# 1、PDF 文本分割
import pdfplumber
# 2、文本向量化
from sentence_transformers import SentenceTransformer
# 3、将向量化数据存入本地 Milvus
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

# 连接到 Milvus
connections.connect(
    alias="default",
    host='localhost',
    port='19530'
)
# 定义集合结构
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384)
]
schema = CollectionSchema(fields, "Knowledge base collection")
collection = Collection("knowledge_base", schema)

# 1、PDF 文本分割
def split_pdf_text(pdf_path):
    texts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                texts.append(text)
    return texts

# 2. 文本向量化
model = SentenceTransformer('all-MiniLM-L6-v2')
def vectorize_texts(texts):
    embeddings = model.encode(texts)
    return embeddings


if __name__ == "__main__":
    # 1、PDF 文本分割
    pdf_path = "/Users/ycwh/Desktop/Python/DeepSeek.pdf"
    split_texts = split_pdf_text(pdf_path)
    print(split_texts)

    # 2. 文本向量化
    vectors = vectorize_texts(split_texts)
    print(vectors)

    # 3. 将向量化数据存入本地 Milvus
    # 转换每个向量为列表
    vectors_list = [vector.tolist() for vector in vectors]
    collection.insert([{"embedding": vector} for vector in vectors_list])
    collection.flush()
