def check(remainder,desired):
    if (remainder >= desired) and desired in (1,2,3):
        return True
    else:
        return False

def player_check(name, remainder, check):
    while True:
        try:
            desired=int(input(f"{name}, 何個の石をとりますか？(1～3個まで選べます)："))
            if check(remainder,desired):
                return desired
            else:
                print("適切な数を入力してください")
        except ValueError:
            print("数字を入力してください")
            
def new_remainder(name, remainder, player_check):
    print(f"{name}の番です。残りの石は{remainder}個です。")
    desired=player_check(name, remainder, check)
    remainder-=desired
    return remainder

def main(remainder, new_remainder):
    print("石取りゲームへようこそ！")
    player1=input("プレイヤー1の名前を入力してください：")
    player2=input("プレイヤー2の名前を入力してください：")
    turn=1
    
    while True:
        if turn%2==1:
            remainder=new_remainder(player1, remainder, player_check)
            if remainder<=0:
                print(f"{player1}が最後の石を取りました。{player1}の負けです！")
                break
        elif turn%2==0:
            remainder=new_remainder(player2, remainder, player_check)
            if remainder<=0:
                print(f"{player2}が最後の石を取りました。{player2}の負けです！")
                break
        turn+=1
        
if __name__=="__main__":
    main(15, new_remainder)











    