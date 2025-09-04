products=["りんご","バナナ","みかん","ぶどう"]
prices=[150,100,80,200]

product_prices={product:price for product, price in zip(products, prices)}

print("商品の価格一覧：")
for product, price in product_prices.items():
    print(f"{product}の価格は{price}円です")