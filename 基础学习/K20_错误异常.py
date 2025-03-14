# 异常处理
# try/except
# 异常捕捉可以使用 try/except 语句。

while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")

print("您输入的数字是：", x)


# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
import sys

try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# try/except...else
# try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。

# else 子句将在 try 子句没有发生任何异常的时候执行。

for arg in sys.argv[1:]:
    try:
        f = open(arg, "r")
    except IOError:
        print("cannot open", arg)
    else:
        print(arg, "has", len(f.readlines()), "lines")
        f.close()


# try-finally 语句
# try-finally 语句无论是否发生异常都将执行最后的代码。
def runoob():
    a = 10
    b = 0
    assert a != b, "a 不能等于 b"
    print("正常执行")


try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("这句话，无论异常是否发生都会执行。")


# 抛出异常
# Python 使用 raise 语句抛出一个指定的异常。

# raise语法格式如下：
# raise [Exception [, args [, traceback]]]
# 其中，Exception 是异常的类型，args 是异常的详细信息，traceback 是异常的追踪信息。

# 以下实例如果 x 大于 5 就触发异常:
try:
    xyz = 7  # 这里可以根据实际情况修改 xyz 的值
    if xyz > 5:
        raise Exception("xyz 不能大于 5。xyz 的值为: {}".format(xyz))
    else:
        print("xyz 的值符合要求。")
except Exception as e:
    print("捕获到异常: {}".format(e))


# 自定义异常
# 你可以通过创建一个新的类来定义自己的异常。
class Error(Exception):
    """Base class for other exceptions"""

    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""

    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""

    pass


# 你可以通过继承 Error 类来定义自己的异常类。
# 然后，你可以通过 raise 语句抛出这些异常。


def my_function(value):
    if value < 0:
        raise ValueTooSmallError("输入值太小")
    elif value > 100:
        raise ValueTooLargeError("输入值太大")
    else:
        return value


# 调用函数并捕获异常
try:
    result = my_function(150)
    print(result)
except ValueTooSmallError as e:
    print(e)
except ValueTooLargeError as e:
    print(e)


# 预定义的清理行为
# 一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。

# 下面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:

for line in open("基础学习/K18_tmp.txt"):
    print(line, end="")

"""
# 以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。

# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
"""

with open("基础学习/K18_tmp.txt") as f:
    for line in f:
        print(line, sep="---", end="")
