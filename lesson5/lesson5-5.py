class Vehicle:
    def __init__(self, name):
        self.name=name
    
    def show_name(self): # このメソッドの名前をnameにしてたらinitのインスタンス変数と重複しているためエラーがでた。
        print(f"この乗り物は{self.name}です。")
        
        
class Car(Vehicle):
    def ride(self):
        print(f"{self.name}が道路を走っています。")
    
class Motorcycle(Vehicle):
    def ride(self):
        print(f"{self.name}が高速道路を疾走しています。")
    
    
car=Car("トヨタ")
car.show_name()
bike=Motorcycle("ハーレー")
bike.show_name()
car.ride()
bike.ride()