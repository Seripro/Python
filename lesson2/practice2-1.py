#ハイアンドローゲーム
import random

player_card=random.randint(1,13)
computer_card=random.randint(1,13)
print("=== ハイアンドローゲームへようこそ！ ===")
print(f"【プレイヤー】{player_card} VS ??【コンピュータ】")
print("あなたのカードはコンピュータのカードより大きい？小さい？")

answer=int(input("1:大きい、2:小さい\n⇒"))

while answer!=1 and answer!=2:
    print("1か2を入力してください")
    answer=int(input("1:大きい、2:小さい\n⇒"))

print(f"【プレイヤー】{player_card} VS {computer_card}【コンピュータ】")

if (answer==1 and player_card > computer_card) or (answer==2 and player_card < computer_card):
    print("正解！あなたの勝ち！")
elif player_card==computer_card:
    print("引き分け")
else:
    print("不正解！あなたの負け！")