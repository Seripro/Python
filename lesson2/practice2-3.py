#じゃんけんゲーム
import random
print("じゃんけんゲームを始めます！")
com=random.randint(0,2)
pla=com
print(com,pla)
while com==pla or (pla!=0 and pla!=1 and pla!=2): #あいこか無効な数字入力の場合繰り返す。
    com=random.randint(0,2) #あいこの場合を考慮して、手を変える。
    try:
        pla=int(input("じゃんけんの手を入力してください（グー: 0, チョキ: 1, パー: 2):"))
    except ValueError:
        print("無効な数字です。")



if pla==0:
    if com==1:
        print("コンピュータの手：チョキ")
        print("あなたの勝ちです！")
    if com==2:
        print("コンピュータの手：パー")
        print("あなたの負けです！")

if pla==1:
    if com==0:
        print("コンピュータの手：グー")
        print("あなたの負けです！")
    if com==2:
        print("コンピュータの手：パー")
        print("あなたの勝ちです！")

if pla==2:
    if com==0:
        print("コンピュータの手：グー")
        print("あなたの勝ちです！")
    if com==1:
        print("コンピュータの手：チョキ")
        print("あなたの負けです！")