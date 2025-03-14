s = "Hello, Runoob"
print(str(s))
print(repr(s))  # repr() 的参数可以是 Python 的任何对象

# sep 分隔符 和 end 以什么结尾 默认 ‘\n’
print("a", "b", "c", sep="----", end="最后呀")
print("\n")

# 输出一个平方与立方的表:
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

print("---------------")
print("12".zfill(5))  # 输出 '00012'


# str.format() 的基本使用如下:
print(
    '{}网址： "{}!"'.format("菜鸟教程", "www.runoob.com")
)  # 菜鸟教程网址： "www.runoob.com!"


# 读取键盘输入
# Python 提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
keyboard_str = input("请输入：")
print("你输入的内容是: ", keyboard_str)
