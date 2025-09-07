from math import pi
while True:
    try:
        r=float(input("半径を入力してください："))
        if r<=0:
            print("正の値を入力してください。")
        else:
            break
    except ValueError:
        print("数字を入力してください。")
        
print("直径：",r*2)
print("面積：",r*r*pi)
print("円周：",r*2*pi)


# メモ　dir(モジュール名)でモジュールに含まれる関数やクラス名を取得できる。

# やっている内容は同じだが、構造が正解コードと全然違った。まだきれいなコードが書けない。今はそこを目指さなくていいのかもしれないが、、、
"""
import math  # 標準モジュール "math" をインポート

def calculate_circle_properties(radius):
    
    # 円の半径を受け取り、直径、面積、円周を計算する関数
    # - math モジュールを使用して数学的な計算を行う

    if radius <= 0:
        # 半径が0以下の場合、エラーメッセージを返す
        return "半径は正の数を入力してください。"
    
    # math モジュールを使用して計算
    diameter = radius * 2					# 直径
    area = math.pi * (radius ** 2)			# 面積
    circumference = 2 * math.pi * radius	# 円周

    # 結果を辞書形式で返す
    return {
        "直径": diameter,
        "面積": area,
        "円周": circumference
    }

try:
    # ユーザーから半径を入力
    radius = float(input("円の半径を入力してください（例: 5）: "))
    # 計算結果を取得
    result = calculate_circle_properties(radius)
    # 結果を表示
    if isinstance(result, str):  # エラーメッセージが返ってきた場合
        print(result)
    else:
        print(f"直径: {result['直径']:.2f}")
        print(f"面積: {result['面積']:.2f}")
        print(f"円周: {result['円周']:.2f}")
except ValueError:
    # 数値以外が入力された場合のエラーメッセージ
    print("数値を入力してください！")
"""