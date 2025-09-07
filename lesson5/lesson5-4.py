# @propertyを使ったゲッター、セッターの定義
# 5-3でのゲッター、セッターと何が違うのか、これの何が便利なのかもわからない。
class Person:
    def __init__(self, name, age):
        self._name=name
        self._age=age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("名前は文字列でなければなりません。")
        self._name=value
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if (not isinstance(value, int)) or value<0:
            raise ValueError("年齢は0以上の整数でなければなりません。")
        self._age=value
    
person=Person("田中",21)
print("名前：",person.name)
print("年齢：",person.age)

person.name="鈴木"
person.age=25

print("新しい名前：",person.name)
print("新しい年齢：",person.age)