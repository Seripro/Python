import random
set1=set(random.sample(range(1,31),10))
set2=set(random.sample(range(1,31),10))
set3=set(random.sample(range(1,31),10))

print("集合1：",set1)
print("集合2：",set2)
print("集合3：",set3)

print("和集合：",set1 | set2 | set3)
print("積集合：",set1 & set2 & set3)
print("差集合（集合1 - 集合2 - 集合3）：",set1 - set2 - set3)