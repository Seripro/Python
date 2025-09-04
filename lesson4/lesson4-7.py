numbers=[1,2,3,4,5,6,7,8,9,10]
numbers2=[]

for number in numbers:
    if number%2==1:
        numbers2.append(number*2)

numbers3=[number*2 for number in numbers if number%2==1]


print(numbers)
print(numbers2)
print(numbers3)
