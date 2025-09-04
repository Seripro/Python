# 答え見た

import random

def game_board(board):
    ue=board[0:3]
    naka=board[3:6]
    shita=board[6:9]
    print("|".join(ue))
    print("--+--+--")
    print("|".join(naka))
    print("--+--+--")
    print("|".join(shita))

def check_win(board, mark):
    WIN_PATTERNS = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # 横
        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # 縦
        (0, 4, 8), (2, 4, 6)                # 斜め
    )

    is_win_results = []
    
    # すべての勝利パターンをチェックし、結果をリストに追加
    for pattern in WIN_PATTERNS:
        # このパターンが勝利条件を満たすかチェック
        is_this_pattern_win = all(board[i] == mark for i in pattern) # patternに入っている三つの数字の組み合わせがすべてmarkと一致するならTrueを返す。
        is_win_results.append(is_this_pattern_win) # TrueかFalseかをリストに追加
        
    # 勝利条件を満たしたパターンが1つでもあればTrueを返す
    return any(is_win_results)

# 引き分けを判定する関数
def check_draw(board):
    return all(space in ("○", "×") for space in board) # boardのすべての要素が○か×だったらTrueを返す

# コンピュータがランダムにマスを選ぶ関数
def computer_move(board):
    available_moves = [i for i, space in enumerate(board) if space not in ("○", "×")] # 〇も×もないマスならインデックスと要素を取り出す。で、リストにはインデックスを収納する。
    return random.choice(available_moves) # 空きマスからランダムで一つ選んで返す。

def play_game():
    board = [str(i) for i in range(1, 10)]  # 1〜9の番号で初期化
    print("マルバツゲームを開始します！")

    while True:
        # 現在のグリッドを表示
        game_board(board)

        # プレイヤーのターン
        while True:
            try:
                player_move = int(input("どのマスに置きますか？（1-9で入力してください）> ")) - 1
                if board[player_move] not in ("○", "×"): # プレイヤーの選んだマスが○と×のどちらでもなければTrue
                    board[player_move] = "○"
                    break
                else:
                    print("そのマスはすでに埋まっています。別のマスを選んでください。")
            except (ValueError, IndexError): # intに変換できないときとインデックスの番号を超えるとき
                print("無効な入力です。1から9の数字を入力してください。")

        # 勝利判定
        if check_win(board, "○"):
            game_board(board)
            print("プレイヤーの勝ちです！")
            break

        # 引き分け判定
        if check_draw(board):
            game_board(board)
            print("引き分けです！")
            break

        # コンピュータのターン
        print("コンピュータのターンです...")
        comp_move = computer_move(board)
        board[comp_move] = "×"
        print(f"コンピュータが選んだマス: {comp_move + 1}")

        # 勝利判定
        if check_win(board, "×"):
            game_board(board)
            print("コンピュータの勝ちです！")
            break

        # 引き分け判定
        if check_draw(board):
            game_board(board)
            print("引き分けです！")
            break

if __name__ == "__main__":
    play_game()
