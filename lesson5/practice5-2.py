from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self, name, hp, attack_power):
        self._name=name
        self._hp=hp
        self._attack_power=attack_power
        
    def get_name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
            self._hp=value
        
    @property
    def attack_power(self):
        return self._attack_power
    
    @attack_power.setter
    def attack_power(self, value):
        if value>0:
            self._attack_power=value
        else:
            raise ValueError("正の値を入力してください。")
        
    def is_alive(self):
        if self.hp>0:
            return True
        else:
            return False
    
    @abstractmethod
    def attack(self, opponent, defend=False):
        pass
    
    @staticmethod
    def damage(target, amount):
        target.hp=target.hp-amount
        
class Player(Character):
    def attack(self, opponent, defend=False):
        print(f"{self.get_name()}の攻撃！")
        Character.damage(opponent, self.attack_power)
        print(f"{opponent.get_name()}に{self.attack_power}のダメージ！")
    
    def defend(self):
        print(f"{self.get_name()}は防御を選んだ！")
        return True
    
class Monster(Character):
    def __init__(self, name, hp, attack_power): # もちろんここの引数にはselfが必要
        super().__init__(name, hp, attack_power) # ここの引数にselfはいらん
        self.attack_chance=60
        
    def attack(self, opponent, defend=False):
        roll=random.randint(1,100)
        print(f"{self.get_name()}の攻撃！")
        if roll <=self.attack_chance:
            if defend:
                print("攻撃は防がれた！")
                self.attack_chance=60
            else:
                print("攻撃が成功！")
                Character.damage(opponent, self.attack_power)
                print(f"{opponent.get_name()}に{self.attack_power}のダメージ！")
                self.attack_chance=60
        else:
            print("攻撃はミス！")
            self.attack_chance+=20
            
def battle_game():
    player=Player("勇者",100,20)
    monster=Monster("ドラゴン",120,25)
    defend=False
    
    while player.is_alive() and monster.is_alive():
        print(f"{player.get_name()}のHP：{player.hp}, {monster.get_name()}のHP：{monster.hp}（成功率：{monster.attack_chance}%）")
        while True:
            try:
                choice=int(input("行動を選んでください（1:攻撃, 2:防御）：").strip())
                if choice==1:
                    player.attack(monster)
                    break
                elif choice==2:
                    defend=player.defend()
                    break
                else:
                    print("1か2を入力してください。")
            except ValueError:
                print("無効な入力です。")
                
        if not monster.is_alive():
            print(f"勝者：{player.get_name()}")
            break
        
        monster.attack(player,defend)
        defend=False
        if not player.is_alive():
            print(f"勝者：{monster.get_name()}")
            
if __name__=="__main__":
    battle_game()