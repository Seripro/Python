# インスタンスの引数が受け取ったデータを出力するのが楽になる。
from dataclasses import dataclass
from math import pi
@dataclass
class Circle:
    radius:float
    
    def area(self):
        return self.radius*self.radius*pi
    
    def circumference(self):
        return 2*self.radius*pi
    
@dataclass # これ忘れたらエラー起きた
class Rectangle:
    width:float #これらの変数をフィールドと呼ぶ
    height:float
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*self.width+2*self.height
    
circle=Circle(radius=3)
rectangle=Rectangle(width=5,height=3)

print("円の半径：",circle.radius)
print(f"円の面積：{circle.area():.2f}") # 小数点以下二桁の表式はreturnで使えないっぽい
print(f"円周の長さ：{circle.circumference():.2f}") # 小数点以下二桁表示はあくまでも文字列

print(f"長方形の幅：{rectangle.width}, 長方形の高さ：{rectangle.height}")
print("長方形の面積：",rectangle.area())
print("長方形の外周：",rectangle.perimeter())
    
    
    
