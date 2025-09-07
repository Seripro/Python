# 静的メソッド
class Book:
    def __init__(self, title, year, author):
        self.title=title
        self.author=author
        self.year=int(year)
        
    def info(self):
        print(f"『{self.title}』（{self.year}）- {self.author}")
    
    @staticmethod
    def is_valid_year(year):
        return isinstance(year,int) and year>0


print(Book.is_valid_year(2020))
print(Book.is_valid_year(-150))

book=Book("吾輩は猫である",1905,"夏目漱石")
book.info()
if Book.is_valid_year(2025): # 静的メソッドはインスタンスを作成しなくても クラス名.メソッド名 で使える。
    book2=Book("未来図書",2025,"AI研究者")
    book2.info()
else:
    print("無効な出版年です。")
