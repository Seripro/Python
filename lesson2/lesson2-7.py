#break,continueについて
for i in range(1,11):
    if i%3==0:
        print(f"{i}は3の倍数なのでスキップします")
        continue
    if i==8:
        print("8に達したのでループを終了します")
        break
    print(f"現在の数字：{i}")
print("ループが終了しました")