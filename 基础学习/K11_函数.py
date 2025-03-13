# 定义函数格式
# def 函数名（参数列表）:
#     函数体


def max(a, b):
    if a > b:
        return a
    else:
        return b


a = 4
b = 5
print(max(a, b))


# 必需参数
# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用 printme 函数，不加参数会报错
printme("参数111111")


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")


# 不定长参数
def printinfo2(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo2函数
printinfo2(70, 60, 50, 40)


# 加了两个星号 ** 的参数会以字典的形式导入
# 可写函数说明
def printinfo3(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo3(1, a=2, b=3)
