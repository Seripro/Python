def calculate_and_print_interest(principal, rate, time):
    interest = principal*pow((1+rate/100),time)
    print(f"{time}年後の預金額は：{round(interest,2)}円です。")
    
    
    
principal=float(input("元金を入力してください："))
rate=float(input("年利(%)を入力してください："))
time=float(input("預ける年数を入力してください："))
calculate_and_print_interest(principal, rate, time)