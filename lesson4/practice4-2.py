import random
players={
    "player":{"tiles":[1,2,3,4,5,6,7,8,9],"score":0},
    "computer":{"tiles":[1,2,3,4,5,6,7,8,9],"score":0}
    }

# 1ターン分の動きを処理し、そのターンの獲得点数、持牌をリターンする関数
def one_game(card_pla, card_com):
    while True:
        try:
            choice_pla=int(input("持ち牌の中から出す牌を選択してください >"))
            if not (choice_pla in card_pla) or not (0 < choice_pla and choice_pla < 10):
                print("持ち牌の中から選んでください。")
                continue
            else:
                break
        except ValueError:
            print("適切な数字を入力してください。")
    
    while True:
        choice_com=random.randint(1,9)
        if choice_com in card_com:
            break
        else:
            continue
        
        
    if choice_pla==choice_com:
        print(f"プレイヤーの打牌：{choice_pla} = {choice_com}：コンピュータの打牌")
        print("両者獲得ポイントなし")
        one_score_pla=0
        one_score_com=0
        return [one_score_pla, one_score_com, choice_pla, choice_com]
    elif choice_pla<choice_com:
        print(f"プレイヤーの打牌：{choice_pla} < {choice_com}：コンピュータの打牌")
        print(f"コンピュータは{choice_com}点獲得")
        one_score_pla=0
        one_score_com=choice_com
        return [one_score_pla, one_score_com, choice_pla, choice_com]
    else:
        print(f"プレイヤーの打牌：{choice_pla} > {choice_com}：コンピュータの打牌")
        print(f"プレイヤーは{choice_pla}点獲得")
        one_score_pla=choice_pla
        one_score_com=0
        return [one_score_pla, one_score_com, choice_pla, choice_com]
    
    # メインの関数
def main_game():
    print("ナインゲームを開始します！")
    # スコア
    score_pla=0
    score_com=0
    
    # 持牌
    card_pla=players["player"]["tiles"]
    card_com=players["computer"]["tiles"]
    
    # one_game関数の戻り値を受け取るリスト
    info=[]
    
    # それぞれの回でのスコアの記録
    score_info={}
    
    # 1～9回戦のループ
    for i in range(9):
        print(f"【第{i+1}回戦】")
        print(f"プレイヤーの得点：{score_pla}点")
        print(f"コンピュータの得点：{score_com}点")
        # ...existing code...
        print(f"☆プレイヤーの持牌⇒【{','.join(str(x) if x != -1 else '-' for x in card_pla)}】")
        print(f"コンピュータの持牌⇒【{','.join(str(x) if x != -1 else '-' for x in card_com)}】")
        # ...existing code...
        info.append(one_game(card_pla, card_com))
        
        score_pla+=info[i][0]
        score_com+=info[i][1]
        
        score_info[i]=(info[i][2], info[i][3])
        
        players["player"]["tiles"][info[i][2]-1]=-1
        players["computer"]["tiles"][info[i][3]-1]=-1
        
        card_pla=players["player"]["tiles"]
        card_com=players["computer"]["tiles"]

    print("ゲーム終了！")
    print("プレイヤーの得点：",score_pla)
    print("コンピュータの得点：",score_com)
    if score_pla==score_com:
        print("引き分けです！")
    elif score_pla>score_com:
        print("プレイヤーの勝利です！")
    else:
        print("コンピュータの勝利です！")
        
    print("=== 対戦履歴 ===")
    for i in range(9):
        print(f"第{i+1}回戦：プレイヤー={score_info[i][0]}, コンピュータ={score_info[i][1]}")

if __name__=="__main__":
    main_game()
    
    
# 正解コード
'''
import random

# タイル（持ち牌）を表示する関数
def display_tiles(title, tiles):
    print(f"{title}⇒【", end="")
    print(" ,".join([str(tile) if tile != -1 else "-" for tile in tiles]), end="")
    print("】")

# プレイヤーとコンピュータの得点を表示する関数
def display_scores(players):
    print(f"プレイヤーの得点　： {players['player']['score']}点")
    print(f"コンピュータの得点： {players['computer']['score']}点")

# プレイヤーが手持ちから牌を選ぶ関数（入力処理付き）
def get_player_choice(tiles):
    while True:
        try:
            choice = int(input("持ち牌の中から出す牌を選択してください > "))
            if choice in tiles:
                return choice
            else:
                print("無効な選択です。再度選択してください。")
        except ValueError:
            print("数字を入力してください。")

# コンピュータがランダムに牌を選ぶ関数
def get_computer_choice(tiles):
    return random.choice(tiles)

# ナインゲームのメイン処理を行う関数
def main():
    # プレイヤーとコンピュータの状態を辞書で管理
    players = {
        "player": {"tiles": [1,2,3,4,5,6,7,8,9], "score": 0},
        "computer": {"tiles": [1,2,3,4,5,6,7,8,9], "score": 0}
    }
    
    # タプルで対戦履歴を残す
    history = []

    print("ナインゲームを開始します！")

    for round_num in range(1, 10):
        print(f"\n【第{round_num}回戦】")

        display_scores(players)

        display_tiles("☆プレイヤーの持ち牌", players["player"]["tiles"])
        display_tiles("コンピュータの持ち牌", players["computer"]["tiles"])

        player_choice = get_player_choice([tile for tile in players["player"]["tiles"] if tile != -1])
        computer_choice = get_computer_choice([tile for tile in players["computer"]["tiles"] if tile != -1])

        print(f"プレイヤーの打牌：{player_choice}", end="")
        if player_choice > computer_choice:
            print(f"　＞　{computer_choice}：コンピュータの打牌")
            players["player"]["score"] += player_choice
            print(f"プレイヤーは{player_choice}点獲得")
        elif player_choice < computer_choice:
            print(f"　＜　{computer_choice}：コンピュータの打牌")
            players["computer"]["score"] += computer_choice
            print(f"コンピュータは{computer_choice}点獲得")
        else:
            print(f"　＝　{computer_choice}：コンピュータの打牌")
            print("引き分けです。得点はなし")

        # 使用済み牌を -1 に
        players["player"]["tiles"][players["player"]["tiles"].index(player_choice)] = -1
        players["computer"]["tiles"][players["computer"]["tiles"].index(computer_choice)] = -1

        # タプルで履歴保存
        history.append((player_choice, computer_choice))

    print("\nゲーム終了！")
    display_scores(players)

    if players["player"]["score"] > players["computer"]["score"]:
        print("プレイヤーの勝利です！")
    elif players["player"]["score"] < players["computer"]["score"]:
        print("コンピュータの勝利です！")
    else:
        print("引き分けです！")

    print("\n=== 対戦履歴（タプル） ===")
    for i, (p, c) in enumerate(history, 1):
        print(f"第{i}回戦: プレイヤー={p}, コンピュータ={c}")

if __name__ == "__main__":
    main()
'''