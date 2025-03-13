
# list 推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names) # ['ALICE', 'JERRY', 'WENDY', 'SMITH']

# set 推导式
numbers = [1,2,3,4,5,6,7,8,9,10]
new_numbers = {num for num in numbers if num%2==0}
print(new_numbers) # {2, 4, 6, 8, 10}

# dict 推导式
d = {'a':1,'b':2,'c':3}
new_d = {k:v**2 for k,v in d.items() if v%2==0}
print(new_d) # {'b': 4} 

# 嵌套推导式
matrix = [[1,2,3],[4,5,6],[7,8,9]]
new_matrix = [[num for num in row if num%2==0] for row in matrix]
print(new_matrix) # [[2], [4, 6], [8]]    

# 条件推导式
numbers = [1,2,3,4,5,6,7,8,9,10]        
new_numbers = [num for num in numbers if num%2==0 if num%3!=0]
print(new_numbers) # [2, 4, 8, 10]

