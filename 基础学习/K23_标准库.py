# Python 标准库非常庞大，所提供的组件涉及范围十分广泛，使用标准库我们可以让您轻松地完成各种任务。

# 以下是一些 Python3 标准库中的模块：

# os 模块：os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。

# sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。

# time 模块：time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。

# datetime 模块：datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。

# random 模块：random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。

# math 模块：math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。

# re 模块：re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。

# json 模块：json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。

# urllib 模块：urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。


# 操作系统接口
# os 模块提供了不少与操作系统相关联的函数，例如文件和目录的操作。
import os

# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)

# 列出目录下的文件
files = os.listdir(current_dir)
print("目录下的文件:", files)


# 文件通配符
# glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:

print("-----------------------")
import glob

# 列出当前目录下所有 .py 文件
print(glob.glob("*.py"))

# 命令行参数
# 通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
print("-----------------------")
import sys

print(sys.argv)


# 日期和时间
# datetime 模块为日期和时间处理同时提供了简单和复杂的方法。
# 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。

print("-----------------------")
import datetime

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45
