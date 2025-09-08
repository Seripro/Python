# 可変長変数　*はタプル、**は辞書
def show_shopping_list(*items):
    print("買い物リストを表示します：")
    for item in items:
        print(f"- {item}")
        
def calculate_total_price(*prices):
    return sum(prices)

show_shopping_list("たまご","パン","牛乳")
total=calculate_total_price(120,350,220)
print(f"合計金額は{total}円です。")