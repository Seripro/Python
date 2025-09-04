
message= lambda x:"大人です" if x>=18 else "未成年です"
age=int(input("年齢を入力してください: "))
print(f"年齢が{age}の場合：{message(age)}")
