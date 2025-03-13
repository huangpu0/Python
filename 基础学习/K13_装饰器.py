# 装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。

# 装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。

# 装饰器的语法使用 @decorator_name 来应用在函数或方法上。

# Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。

# 装饰器的应用场景：

# 日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
# 性能分析: 可以使用装饰器来测量函数的执行时间。
# 权限控制: 装饰器可用于限制对某些函数的访问权限。
# 缓存: 装饰器可用于实现函数结果的缓存，以提高性能。


# Python 装饰允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能，
# 装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。


def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        before_call_code()

        result = original_function(*args, **kwargs)

        # 这里是在调用原始函数后添加的新功能
        after_call_code()

        print("result", result)
        return result

    print("wrapper", wrapper)
    return wrapper


print("decorator_function", decorator_function)


def before_call_code():
    print("Before call code")
    pass  # 新功能代码


def after_call_code():
    print("After call code")
    pass  # 新功能代码


# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    pass  # 原始函数的实现


target_function(1, 2)  # 输出：Before call code, After call code
