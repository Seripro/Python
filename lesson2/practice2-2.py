#数字あてゲーム
import random
correct_number=random.randint(1,100)
max_attempts=10
print("1から100までの数字を当ててください！")
print("あなたには10回のチャンスがあります。")
is_correct=False #正解したかどうかのフラグ

for i in range(10):
    try:
        player_number=int(input("あなたの予測："))
    except ValueError:
        print("整数を入力してください")
    if player_number==correct_number:
        print(f"おめでとうございます！正解です！{i+1}回目で当てました。")
        break
    elif player_number > correct_number:
        print("もっと小さい数字です。")
    else:
        print("もっと大きい数字です。")
    max_attempts=max_attempts-1
    print(f"残りのチャンスは{max_attempts}回です。")

if max_attempts==0 and is_correct==False:
    print(f"正解は{correct_number}でした。")

print("ゲームを終了します。")