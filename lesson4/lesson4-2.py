fruits=["りんご","バナナ","みかん","いちご","ぶどう"]
fruits.clear()
print(fruits) # []
fruits=["りんご","バナナ","みかん","いちご","ぶどう"]
fruits.remove("バナナ")
print(fruits) # ['りんご', 'みかん', 'いちご', 'ぶどう']
print(fruits.pop(2)) # いちご
print(fruits) # ['りんご', 'みかん', 'ぶどう']
del fruits[1]
print(fruits) # ['みかん', 'いちご']