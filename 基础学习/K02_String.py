# 字符串的基本操作学习
import time

# 进度条效果
for i in range(101):
    print("\r{:3}%".format(i),end=' ')
    time.sleep(0.05)
 
x="a"
y="b"
# 换行输出
print( x )
print( y )
print(x,y)  # 输出两个字符串
print(x+y)  # 连接两个字符串
print('---------')  

# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
print('---------')  

# 定义一个字符串
str = 'Runoob'  # 定义一个字符串变量
print(str)           # 打印整个字符串
print(str[0:-1])     # 打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str[0])        # 打印字符串的第一个字符
print(str[2:5])      # 打印字符串第三到第五个字符（包含第五个字符）
print(str[2:])       # 打印字符串从第三个字符开始到末尾
print(str * 2)       # 打印字符串两次
print(str + "TEST")  # 打印字符串和"TEST"拼接在一起
print(str.capitalize())  # 首字母大写
print(str.upper())        # 全部大写
print(str.lower())        # 全部小写
print(str.replace("o", "O"))  # 替换字符
print(str.split("o"))  # 以字符o分割字符串 返回列表
print(str.startswith("h"))  # 字符串以字符h开头 返回bool值
print(str.endswith("g"))    # 字符串以字符g结尾 返回bool值
print(str.find("n"))       # 字符串中第一次出现字符n的位置 返回int值
print(str.count("n"))      # 字符串中字符n出现的次数 返回int值
print(str.isalnum())       # 字符串中所有字符都是字母或数字 返回bool值
print(str.isalpha())       # 字符串中所有字符都是字母 返回bool值
print(str.isdigit())       # 字符串中所有字符都是数字 返回bool值
print(str.islower())       # 字符串中所有字符都是小写 返回bool值
print(str.isupper())       # 字符串中所有字符都是大写 返回bool值

