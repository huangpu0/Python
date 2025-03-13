import sys

# 导入模块
import K01_Number

# 现在可以调用模块里包含的函数了
result = K01_Number.cus_max(10, 20)
print("自定义的最大值是：", result)

print("命令行参数如下:")
for i in sys.argv:
    print(i)

print("当前Python 路径为：", sys.path, "\n")


# from … import 语句
# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

from K01_Number import cus_max

# 这行代码将 K01_Number 模块中的 cus_max 函数导入到当前命名空间中，你可以直接使用这个函数了。
print(cus_max(1011, 20))


# 给模块起别名
# 使用 as 关键字为模块或函数起别名：
import K01_Number as first  # 将 k01_number 模块别名设置为 frist

first.cus_max(10, 100)  # 调用别名为 first 的模块中的 cus_max 函数


# 模块的 __name__ 属性是一个字符串，它的值是模块的名字。当模块被直接运行时，__name__ 的值为 "__main__"。
# 每个模块都有一个 __name__ 属性。

if __name__ == "__main__":
    print("程序自身在运行")
else:
    print("我来自另一模块")


# 标准模块
# Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。

# 模块名	功能描述
# math	数学运算（如平方根、三角函数等）
# os	操作系统相关功能（如文件、目录操作）
# sys	系统相关的参数和函数
# random	生成随机数
# datetime	处理日期和时间
# json	处理 JSON 数据
# re	正则表达式操作
# collections	提供额外的数据结构（如 defaultdict、deque）
# itertools	提供迭代器工具
# functools	高阶函数工具（如 reduce、lru_cache）
