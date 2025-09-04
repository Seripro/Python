import random 

def win_or_lose(cho_and_han, result):
    if cho_and_han==0 and result=="丁" or cho_and_han==1 and result=="半":
        return "あなたの勝ち！"
    else:
        return "あなたの負け！"


my_money=1000

print("丁半賭博ゲームを始めます！")

while True:
    print(f"プレイヤーの所持金：{my_money}円")
    while True:
        try:
            bet_money=int(input("いくら賭けますか？⇒"))
            if bet_money>my_money or bet_money<=0:
                print("適切な金額を入力してください")
            else:
                break
        except ValueError:
            print("数字を入力してください")

    while True:
        try:
            cho_and_han=int(input("丁(0)か半(1)を選んでください⇒"))
            if cho_and_han!=0 and cho_and_han!=1:
                print("0か1を入力してください")
            else:
                break
        except ValueError:
            print("数字を入力してください")
            
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    result=lambda x,y: "丁" if (x+y) % 2 == 0 else "半"
    print(f"サイコロの目：{dice1},{dice2} ⇒ {result(dice1,dice2)}")
    
    if win_or_lose(cho_and_han, result(dice1,dice2))=="あなたの勝ち！":
        my_money+=bet_money
        print(f"{win_or_lose(cho_and_han, result(dice1,dice2))}賞金は{bet_money}円")

    else:
        print(f"{win_or_lose(cho_and_han, result(dice1,dice2))}賞金は0円")
        my_money-=bet_money
    if my_money<=0:
        print("所持金が0円になりました。ゲームオーバーです")
        break
    print(f"プレイヤーの所持金：{my_money}円")
    continue_game=int(input("続けますか？(はい：０, いいえ：１) ⇒"))
    if continue_game==1:
        break
    
print(f"最終所持金は{my_money}円でした。")
print("丁半賭博ゲームを終了します。")
    
    

