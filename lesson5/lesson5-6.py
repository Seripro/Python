# オーバーライド
class Appliance:
    def __init__(self, name):
        self.name=name
    
    def operate(self):
        print("家電で操作を開始します。")
        
class WashingMachine(Appliance):
    def operate(self): # オーバーライドは親クラスのメソッドを上書きするので、親を維持したいときはsuper()を使う。
        print(f"洗濯機で洗濯を開始します。")
        
class Refrigerator(Appliance):
    def operate(self):
        print("冷蔵庫で冷蔵を開始します。")
        
WM=WashingMachine("冷蔵庫")
R=Refrigerator("冷蔵庫")

WM.operate()
R.operate()