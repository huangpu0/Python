
#集合（Set）是由一个或数个元素组成的无序集合。集合中不允许有重复元素，而且元素不能被修改。
set([1,2,3,2,1]) # {1, 2, 3}

set1 = {1,2,3}
set2 = {2,3,4}
set2.add(5)
print(set2) # {2, 3, 4, 5}
set2.remove(5)
print(set2) # {2, 3, 4}         


#集合的基本操作：
#1. 并集：union()
print(set1.union(set2)) # {1, 2, 3, 4}
#2. 交集：intersection()
print(set1.intersection(set2)) # {2, 3}
#3. 差集：difference()
print(set1.difference(set2)) # {1}
#4. 对称差集：symmetric_difference()
print(set1.symmetric_difference(set2)) # {1, 4}
#5. 子集测试：issubset()
print(set1.issubset(set2)) # False
#6. 超集测试：issuperset()
print(set2.issuperset(set1)) # True
#7. 并集更新：update()
print(set1.update(set2)) # None
#8. 交集更新：intersection_update()
print(set1.intersection_update(set2)) # None
#9. 差集更新：difference_update()
print(set1.difference_update(set2)) # None
#10. 对称差集更新：symmetric_difference_update()  
print(set1.symmetric_difference_update(set2)) # None

#集合的应用：
#1. 去重：set(list)
list1 = [1,2,3,2,1]
list2 = list(set(list1))
print(list2) # [1, 2, 3]
#2. 交集：set1 & set2
set1 = {1,2,3}
set2 = {2,3,4}
print(set1 & set2) # {2, 3}
#3. 并集：set1 | set2
print(set1 | set2) # {1, 2, 3, 4}
#4. 差集：set1 - set2
print(set1 - set2) # {1}
#5. 对称差集：set1 ^ set2   
print(set1 ^ set2) # {1, 4}