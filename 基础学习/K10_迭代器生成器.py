
# 迭代器生成器是一种特殊的生成器，它返回一个迭代器对象。
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素 1
print (next(it))   # 输出迭代器的下一个元素 2

for x in it:  # 输出迭代器的下一个元素 3、4
    print (x, end=" ")


# 创建一个迭代器
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
# 如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)

print('\n---------')
# 输出迭代器的下一个元素 1、2、3、4、5
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# 生成器函数是一种特殊的函数，它使用 yield 语句返回一个生成器对象。
# 生成器函数的调用不会执行函数体内的代码，而是返回一个生成器对象。
def countdown(n):
    while n > 0:
        yield n
        n -= 1
 
# 创建生成器对象
generator = countdown(5)
 
print('---------')
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
 
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1
