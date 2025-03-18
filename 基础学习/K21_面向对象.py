# 面向对象技术简介
# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 方法：类中定义的函数。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 局部变量：定义在方法中的变量，只作用于当前实例的类。
# 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。


class MyClass:
    """一个简单的类实例"""

    i = 12345

    def f(self):
        return "hello world"


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

print("----------------")


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


y = Complex(3.0, -4.5)
print(y.r, y.i)  # 输出结果：3.0 -4.5

# self 代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

print("----------------")


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

# 继承
# Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:

# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# 子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。

# BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

print("----------------")


# 类定义
class people:
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ""

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student("ken", 10, 60, 3)
s.speak()

# 方法重写
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：

print("----------------")


class Parent:  # 定义父类
    def myMethod(self):
        print("调用父类方法")


class Child(Parent):  # 定义子类
    def myMethod(self):
        print("调用子类方法")


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法


# 类属性与方法
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

# 类的方法
# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

# self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。

# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。

print("----------------")


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

    def __foo(self):  # 私有方法
        print("这是私有方法")

    def foo(self):  # 公共方法
        print("这是公共方法")
        self.__foo()


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__foo())  # 调用私有方法
print(counter.__secretCount)  # 报错，实例不能访问私有变量
