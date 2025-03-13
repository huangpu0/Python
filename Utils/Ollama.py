
# Ollama 本地大模型的调用示例
import requests 

# 通用模型调用示例
# url  = "http://localhost:11434/api/generate" 
# data = { 
#     "model": "deepseek-r1", 
#     "prompt": "你好，DeepSeek？",
#     "stream": False,
#     } 
# response = requests.post(url, json=data) 

# print(response.text)

# 输出结果：流的形式
# for line in response.iter_lines(): 
#     if line:
#         print(line.decode('utf-8'))


# 聊天模型调用示例
chat_url  = "http://localhost:11434/api/chat" 
chat_data = { 
    "model": "deepseek-r1:14b", 
    "messages": [
    { "role": "system", 
     "content": "云创在广东省、宝安区、是一个印刷行业、有160多人呀哈哈" },
    { "role": "user", 
     "content": "云创有多少人？" }
  ],
    "stream": False,
    #"format": "json"  # 指定输出格式为 JSON
    } 
chat_response = requests.post(chat_url, json=chat_data) 

print(chat_response.text)

# 输出结果：流的形式
# for line in chat_response.iter_lines(): 
#     if line:        
#         print(line.decode('utf-8'))
