# オブジェクト指向
class Animal:
    def __init__(self,name):
        self.name=name
        
    def introduce(self):
        print(f"こんにちは！私は{self.name}です。")
    
Cat=Animal("ネコ")
Dog=Animal("イヌ")
Cat.introduce()
Dog.introduce()