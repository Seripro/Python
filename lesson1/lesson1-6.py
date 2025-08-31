import random
# 0.0 以上 1.0 未満のランダムな数を生成
x=random.random()
print(x)

#1から6のランダムな整数を生成
n=random.randint(1,6)
print(n)

#リストの中身をシャッフル
y=[1,2,3,4,5,6]
print(f"シャッフル前：{y}")
random.shuffle(y)
print(f"シャッフル後：{y}")

#ランダムで一つ選ぶ
alpha=["a","b","c","d","e","f"]
print(random.choice(alpha))

#ランダムで複数選ぶ(重複あり)
print(random.choices(alpha,k=4))

#ランダムで複数選ぶ(重複なし)
print(random.sample(alpha,k=4))

