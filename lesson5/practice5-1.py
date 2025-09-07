# モンスター捕獲ゲーム
# サイコロを振るかどうかを後出しできる仕様にしなかった。間違えた。
# 改善点：重複処理の関数化、main関数でゲーム進行を関数化
from abc import ABC,abstractmethod
import random

class Dice:
    @staticmethod
    def dice(name):
        dice_number=random.randint(1,6)
        print(f"{name}がサイコロを振った。出目は{dice_number}")
        return dice_number


class Monster(ABC):
    def __init__(self,name,hp):
        self._name=name
        self._hp=hp
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("名前は文字列でなければなりません。")
        self._name=value
    
    def dice(self):
        return Dice.dice(self.name)
    
    def message(self):
        print(f"{self.name}が現れた！")
        
    

    
class Slime(Monster):
    pass

class Goblin(Monster):
    pass

class Dragon(Monster):        
    def dice(self):
        Benchmark=1
        for i in range(2):
            dice_number=random.randint(1,6)
            if dice_number>Benchmark:
                Benchmark=dice_number
        print(f"{self.name}がサイコロをふった。出目は{Benchmark}")
        return Benchmark
            
slime=Slime("スライム",30)
goblin=Goblin("ゴブリン",50)
dragon=Dragon("ドラゴン",100)

catch_list=[]
game_over=False

slime.message()
while True:
    yes_or_no=input("サイコロを振りますか？(y/n)：").strip().lower() # stripは前後のスペースを削除。lowerはすべての文字を小文字に変換
    if yes_or_no=="y":
        dice_s=slime.dice()
        dice_p=random.randint(1,6)
        print(f"プレイヤーがサイコロを振った。出目は{dice_p}")
        if dice_s<dice_p:
            print(f"{slime.name}を捕まえた！")
            catch_list.append(slime.name)
        elif dice_s==dice_p:
            print("引き分け")
        else:
            game_over=True
            print(f"{slime.name}を捕まえられなかった。ゲームオーバー！")
        break
    elif yes_or_no=="n":
        break
    else:
        print("yかnを入力してください。")
        continue



if not game_over:
    goblin.message()
    while True:
        yes_or_no=input("サイコロを振りますか？(y/n)：")
        if yes_or_no=="y":
            dice_g=goblin.dice()
            dice_p=random.randint(1,6)
            print(f"プレイヤーがサイコロを振った。出目は{dice_p}")
            if dice_g<dice_p:
                print(f"{goblin.name}を捕まえた！")
                catch_list.append(goblin.name)
            elif dice_g==dice_p:
                print("引き分け")
            else:
                game_over=True
                print(f"{goblin.name}を捕まえられなかった。ゲームオーバー！")
            break
        elif yes_or_no=="n":
            break
        else:
            print("yかnを入力してください。")
            continue
        
if not game_over:
    dragon.message()
    while True:
        yes_or_no=input("サイコロを振りますか？(y/n)：")
        if yes_or_no=="y":
            dice_d=dragon.dice()
            dice_p=random.randint(1,6)
            print(f"プレイヤーがサイコロを振った。出目は{dice_p}")
            if dice_d<dice_p:
                print(f"{dragon.name}を捕まえた！")
                catch_list.append(dragon.name)
            elif dice_d==dice_p:
                print("引き分け")
            else:
                game_over=True
                print(f"{dragon.name}を捕まえられなかった。ゲームオーバー！")                
            break
        elif yes_or_no=="n":
            break
        else:
            print("yかnを入力してください。")
            continue
   


if not game_over:
    print("ゲーム終了！")
    
if not catch_list==[]:     
    print("=== 獲得モンスター ===")
    print(",".join(catch_list))
else:
    print("モンスターを捕まえられなかった。")
    
    
# copilotでリファクタリングした結果
"""
from abc import ABC, abstractmethod
import random

class Dice:
    @staticmethod
    def dice(name):
        dice_number = random.randint(1, 6)
        print(f"{name}がサイコロを振った。出目は{dice_number}")
        return dice_number

class Monster(ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("名前は文字列でなければなりません。")
        self._name = value

    def dice(self):
        return Dice.dice(self.name)

    def message(self):
        print(f"{self.name}が現れた！")

class Slime(Monster):
    pass

class Goblin(Monster):
    pass

class Dragon(Monster):
    def dice(self):
        benchmark = max(random.randint(1, 6), random.randint(1, 6))
        print(f"{self.name}がサイコロをふった。出目は{benchmark}")
        return benchmark

def play_turn(monster, catch_list):
    monster.message()
    while True:
        yes_or_no = input("サイコロを振りますか？(y/n)：")
        if yes_or_no == "y":
            dice_m = monster.dice()
            dice_p = random.randint(1, 6)
            print(f"プレイヤーがサイコロを振った。出目は{dice_p}")
            if dice_m < dice_p:
                print(f"{monster.name}を捕まえた！")
                catch_list.append(monster.name)
                return False  # ゲームオーバーではない
            elif dice_m == dice_p:
                print("引き分け")
                return False
            else:
                print(f"{monster.name}を捕まえられなかった。ゲームオーバー！")
                return True  # ゲームオーバー
        elif yes_or_no == "n":
            return False
        else:
            print("yかnを入力してください。")

def main():
    slime = Slime("スライム", 30)
    goblin = Goblin("ゴブリン", 50)
    dragon = Dragon("ドラゴン", 100)

    catch_list = []
    game_over = False

    for monster in [slime, goblin, dragon]:
        if not game_over:
            game_over = play_turn(monster, catch_list)

    if not game_over:
        print("ゲーム終了！")

    if catch_list:
        print("=== 獲得モンスター ===")
        print(",".join(catch_list))
    else:
        print("モンスターを捕まえられなかった。")

if __name__ == "__main__":
    main()
"""




# 正解コード

'''
import random
from abc import ABC, abstractmethod

# サイコロクラス（ユーティリティ）
class Dice:
    @staticmethod
    def roll():
        return random.randint(1, 6)

# モンスター基底クラス（抽象クラス）
class Monster(ABC):
    def __init__(self, name: str, hp: int = 10):
        self._name = name      # プライベート属性（名前）
        self._hp = hp          # プライベート属性（HP）

    def get_name(self):
        return self._name

    def get_hp(self):
        return self._hp

    def set_hp(self, value: int):
        if value >= 0:
            self._hp = value
        else:
            print("HPは0以上でなければなりません")

    def dice_roll(self):
        return Dice.roll()

    @abstractmethod
    # 各モンスターが持つ特別な動きを表現する抽象メソッド
    def special_move(self):
        pass

# スライムクラス（Monsterを継承）
class Slime(Monster):
    def special_move(self):
        return f"{self.get_name()}は体当たりを仕掛けた！"

# ゴブリンクラス（Monsterを継承）
class Goblin(Monster):
    def special_move(self):
        return f"{self.get_name()}は棍棒を振り回した！"

# ドラゴンクラス（オーバーライドあり）
class Dragon(Monster):
    def dice_roll(self):
        # ドラゴンは2回振って大きい方を採用
        roll1, roll2 = Dice.roll(), Dice.roll()
        return max(roll1, roll2)

    def special_move(self):
        return f"{self.get_name()}は火を吹いた！"

# ゲーム本体
class MonsterCaptureGame:
    def __init__(self):
        self.monsters = [Slime("スライム"), Goblin("ゴブリン"), Dragon("ドラゴン")]
        self.captured_monsters = []

    def play(self):
        for monster in self.monsters:
            print(f"{monster.get_name()}が現れた！")
            print(monster.special_move())

            monster_roll = monster.dice_roll()
            print(f"{monster.get_name()}がサイコロを振った。出目は {monster_roll}")

            response = input("サイコロを振りますか？ (yes/no): ").strip().lower()
            if response == "no":
                print(f"{monster.get_name()}をスキップしました。")
                continue  # 次のモンスターへ

            player_roll = Dice.roll()
            print(f"プレイヤーがサイコロを振った。出目は {player_roll}")

            if player_roll > monster_roll:
                print(f"{monster.get_name()}を捕まえた！")
                self.captured_monsters.append(monster.get_name())
            elif player_roll == monster_roll:
                print("引き分けでもう一度！")
                # 再戦扱いで同じモンスターに再挑戦
                continue
            else:
                print(f"{monster.get_name()}を捕まえられなかった。ゲームオーバー！")
                break

        print("捕まえたモンスター: " + ", ".join(self.captured_monsters))
        print("ゲーム終了")

# 実行
if __name__ == "__main__":
    game = MonsterCaptureGame()
    game.play()
'''