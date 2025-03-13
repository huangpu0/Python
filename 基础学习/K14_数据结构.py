# 将列表当做栈使用

print("---------------------------")
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # 输出: [1, 2, 3]

top_element = stack.pop()
print(top_element)  # 输出: 3
print(stack)  # 输出: [1, 2]

top_element = stack[-1]
print(top_element)  # 输出: 2

is_empty = len(stack) == 0
print(is_empty)  # 输出: False

size = len(stack)
print(size)  # 输出: 2


# 将列表当作队列使用
from collections import deque

# 创建一个空队列
queue = deque()

# 向队尾添加元素
queue.append("a")
queue.append("b")
queue.append("c")

print("---------------------------")
print("队列状态:", queue)  # 输出: 队列状态: deque(['a', 'b', 'c'])

# 从队首移除元素
first_element = queue.popleft()
print("移除的元素:", first_element)  # 输出: 移除的元素: a
print("队列状态:", queue)  # 输出: 队列状态: deque(['b', 'c'])

# 查看队首元素（不移除）
front_element = queue[0]
print("队首元素:", front_element)  # 输出: 队首元素: b

# 检查队列是否为空
is_empty = len(queue) == 0
print("队列是否为空:", is_empty)  # 输出: 队列是否为空: False

# 获取队列大小
size = len(queue)
print("队列大小:", size)  # 输出: 队列大小: 2


# 列表推导式
print("---------------------------")
vec = [2, 4, 6]
print([3 * x for x in vec])  # 输出: [6, 12, 18]
print([[x, x**2] for x in vec])  # 输出: [[2, 4], [4, 16], [6, 36]]


# del 语句
# 使用 del 语句可以从一个列表中根据索引来删除一个元素，而不是值来删除元素。
# 这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，
# 或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。例如：
print("---------------------------")
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)  # 输出: [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)  # 输出: [1, 66.25, 1234.5]
del a[:]
print(a)  # 输出: []
