# タプルのアンパック
person=("佐藤",30,"エンジニア")
name, age, profession = person
print("名前：",name)
print("年齢：",age)
print("職業",profession)

nested_tuple=(("田中",28,"デザイナー"),("鈴木",25,"プログラマー"),("高橋",32,"マネージャー"))

for name, age, profession in nested_tuple:
    print("名前：",name)
    print("年齢：",age)
    print("職業",profession)