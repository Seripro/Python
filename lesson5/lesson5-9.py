# 抽象クラス
from abc import ABC, abstractmethod
class Animal(ABC): # 抽象クラスはインスタンス化できない。継承する前提で作られている。設計図のような目的で使う？
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "ワンワン"
    
    def move(self):
        return "走り回る"
    
class Bird(Animal):
    def make_sound(self):
        return "ぴよぴよ"
    
    def move(self):
        return "空を飛ぶ"
    
dog=Dog()
bird=Bird()

print("犬の鳴き声：",dog.make_sound())
print("犬の移動方法：",dog.move())
print("鳥の鳴き声：",bird.make_sound())
print("鳥の移動方法：",bird.move())