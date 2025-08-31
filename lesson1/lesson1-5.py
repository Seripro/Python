#フォーマット文字列について
import math
pi=math.pi
print(f"{pi:.3f}") #小数点以下3桁を表示　4桁以下は四捨五入

number=3
print(f"{number:02}") #二桁で返す。一桁の場合は先頭に0をつける

#練習問題
name=input("名前を入力してください：")
age=input("年齢を入力してください：")
print(f"こんにちは、{name}さん。あなたは{age}歳ですね。")


