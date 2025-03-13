from pymilvus import connections
import random

# 连接到 Milvus
try:
    # 连接到本地 Milvus
    connections.connect(alias="default", host="localhost", port="19530")

    # query_vector = [random.random() for _ in range(4)]
    # print(query_vector)

    # # 连接到阿里云 Milvus
    # connections.connect(
    #     host='c-e4cd9122cafde16e.milvus.aliyuncs.com',
    #     user='root',
    #     password='Root@123',
    #     port=19530
    # )
    print("Connected to Milvus!")
except Exception as e:
    print(f"Failed to connect to Milvus: {e}")
