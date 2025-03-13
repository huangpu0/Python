# 列表是一种有序集合，它可以包含不同的数据类型，可以随时添加或删除其中的元素。


# 列表类型
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2, 'kaslklakslds', 'skalkdla']  # 定义一个列表
tinylist = [123, 'runoob']

print (list)            # 打印整个列表
print (list[0])         # 打印列表的第一个元素
print (list[-1])        # 打印列表的最后一个元素
print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list[2:])        # 打印列表从第三个元素开始到末尾
print (tinylist * 2)    # 打印tinylist列表两次
print (list + tinylist)  # 打印两个列表拼接在一起的结果
print (len(list))        # 打印列表的长度

# 列表方法
list.append('new')      # 在列表末尾添加一个元素
list.insert(2, 'insert')  # 在列表的第3个位置插入一个元素
list.pop()             # 删除列表末尾的元素
list.pop(2)            # 删除列表的第3个元素
list.remove('abcd')    # 删除列表中值为'abcd'的元素 
list.reverse()         # 反转列表元素的顺序

# 过滤出my_list中的字符串元素，准备排序
string_elements = [element for element in list if isinstance(element, str)]
string_elements.sort()    # 对字符串元素进行排序
print(string_elements)      # 打印排序后的字符串元素

# 列表的切片操作
del list[2]            # 删除列表的第3个元素

print (list)           # 打印修改后的列表

