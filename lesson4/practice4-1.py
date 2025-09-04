# 答え見た

import random

# グリッド、チャンスの回数を受け取る関数
def input_method():
    while True:
        try:
            LEN = int(input("グリッドの一辺の長さを入力してください(1-9の数字)：")) # 10以上をokしてしまうとこの後の二けた表示のところで不具合発生
            if LEN<1 or 9<LEN:
                print("1以上9以下の数字を入力してください")
                continue
            
            chances = int(input("チャンスの回数を入力してください："))
            if chances<1:
                print("無効な数字です。")
                continue
            else:
                break
            
        except ValueError:
            print("数字を入力してください。")
            
    return LEN, chances

# LEN×LENのグリッドを初期化する関数
def initialize_grid(LEN):
    grid=[]
    count=1
    for i in range(LEN): # LEN行分ループ
        row=[]
        for j in range(LEN): # LEN列分ループ
            row.append(f"{count:02d}") # 2桁表示で数字を追加
            count+=1
        grid.append(row)
    return grid

# グリッドを表示する関数
def display_grid(grid):
    print("現在のグリッド：")
    for row in grid:
        print(" ".join(row)) # リスト→文字列に変換して表示
    print()  # 空行を追加して見やすくする

# ヒントを提供する関数
def give_hint(player_x, player_y, treasure_x, treasure_y):
    hint=[]
    if player_x < treasure_x:
        hint.append("右")
    elif player_x > treasure_x:
        hint.append("左")
    if player_y < treasure_y:
        hint.append("下")
    elif player_y > treasure_y:
        hint.append("上")
    
    return "".join(hint)+"に宝があります。" # リスト→文字列の変換

# メインのゲームループ
def treasure_hunt_game(LEN, chances):
    # グリッドと宝の位置を初期化
    grid=initialize_grid(LEN)
    treasure_x=random.randint(0, LEN-1)
    treasure_y=random.randint(0, LEN-1)
    
    # 選択済みマスを集合で記録
    chosen_cells=set()
    
    print(f"宝探しゲームへようこそ！1から{LEN*LEN}までの数字で宝を探し当ててください。")
    print(f"宝を探すチャンスは{chances}回です。")
    display_grid(grid)
    
    attempts=1
    found_treasure=False # 宝を当てたらTrueになり、whileを抜け出す。
    
    while attempts <= chances and not found_treasure:
        try:
            choice = int(input(f"宝の場所を当ててください（1-{LEN*LEN}の数字）："))
            if choice < 1 or choice > LEN*LEN:
                print(f"1から{LEN*LEN}までの数字を入力してください。")
                continue
            
            # 入力をグリッドの座標に変換　このアルゴリズム重要
            player_x = (choice - 1) % LEN
            player_y = (choice - 1) // LEN
            
            # すでに選択されているか確認
            if (player_x, player_y) in chosen_cells:
                print("そのマスはすでに選択されています。別のマスを選んでください。")
                continue
            
            # 選択済みに追加
            chosen_cells.add((player_x,player_y)) # 集合にタプルを追加
            
            # 宝を見つけた場合
            if player_x == treasure_x and player_y == treasure_y:
                print("🎉 おめでとうございます！宝を見つけました！ 🎉")
                grid[player_y][player_x] = "💎"
                found_treasure = True
            else:
                grid[player_y][player_x] = "❌"
                print(give_hint(player_x, player_y, treasure_x, treasure_y))
                print(f"残りのチャンスは{chances-attempts}回です。")
                attempts +=1
                
            display_grid(grid) # グリッドを表示
        
        except ValueError:
            print(f"無効な入力です。1から{LEN*LEN}までの数字を入力してください。")
        
    if not found_treasure:
        print("残念！チャンスがなくなりました。宝は見つかりませんでした。")
        grid[treasure_y][treasure_x] = "💎"
        display_grid(grid)
        
if __name__ == "__main__":
    while True:
        treasure_hunt_game(*input_method()) # 二つの戻り値はタプルで返されるので、引数に入力するために*でタプル解除
        play_again = input("もう一度遊びますか？ (y/n): ")
        if play_again.lower() != 'y':
            break