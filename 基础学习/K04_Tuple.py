
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号 ( )，列表使用方括号 [ ]。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

# 创建元组
t = (1, 2, 3, 4, 5)
print(t)

# 访问元组中的元素
print(t[0])
print(t[1])
print(t[-1])

# 元组的不可变性
# 元组中的元素不能修改，所以不能对元组进行 append()、insert()、pop() 等修改操作。
# 但是，可以对元组进行切片操作，得到一个新的元组。

# 元组的拆包
# 元组也可以进行拆包，即将元组中的元素赋值给多个变量。
a, b, c, d, e = t
print(a, b, c, d, e)

# 元组的比较
# 元组之间可以进行比较，如果元组中元素的个数、顺序都相同，则认为两个元组相等。
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)
print(t1 == t2)  # True
print(t1 == t3)  # False

# 元组的嵌套
# 元组可以嵌套，即一个元组可以包含另一个元组。
t4 = (1, 2, (3, 4, 5))
print(t4[2][1])  # 4
print("-------------")

# 元组的遍历
# 元组也可以进行遍历，可以使用 for 循环来遍历元组中的元素。
for i in t: 
    print(i)    
