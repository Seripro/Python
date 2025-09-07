# プライベート属性、ゲッター、セッター　　まだ簡単

class Product:
    def __init__(self, name, price):
        self._name=name
        self._price=price
        
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if price<=0:
            print("価格は0より大きい値を設定してください。")
        else:
            self._price=price
                
apple=Product("りんぎ",100)
print("商品名：",apple.get_name())
print("価格：",apple.get_price())

apple.set_price(120)
print("新しい価格：",apple.get_price())

apple.set_price(0)