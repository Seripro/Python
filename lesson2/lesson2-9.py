#例外処理
num1=int(input("一つ目の整数を入力してください："))
num2=int((input("二つ目の整数を入力してください：")))
try:
    num3=num1/num2
    print(num3)
except ZeroDivisionError:
    print("0で割ることはできません。")
except ValueError:
    print("整数ではありません。")
finally:
    print("処理を終了しました。")

