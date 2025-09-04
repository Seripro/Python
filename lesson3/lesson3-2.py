def calculate_total(price, quantity=1):
    return price * quantity

price=int(input("商品の価格を入力してください（円）："))
quantity=input("商品の数量を入力してください（省略すると1になります）：")

if quantity=="":
    print(f"合計金額は{calculate_total(price)}円です。")
else:
    print(f"合計金額は{calculate_total(price, int(quantity))}円です。")



