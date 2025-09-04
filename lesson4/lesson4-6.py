numbers=[1,2,3,4,5,6,7,8,9]
squared_numbers=[]

for number in numbers:
    squared_numbers.append(number**2)

print(f"{squared_numbers[0]},{squared_numbers[1]},{squared_numbers[2]}")
print(f"{squared_numbers[3]},{squared_numbers[4]},{squared_numbers[5]}")
print(f"{squared_numbers[6]},{squared_numbers[7]},{squared_numbers[8]}")

'''
こっちの方がきれいだった、、
for i in range(0, len(squared_numbers), 3):
    # リストを3つずつ表示
    print(f"{squared_numbers[i]},{squared_numbers[i+1]},{squared_numbers[i+2]}")
'''