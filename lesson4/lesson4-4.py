scores=[88,74,95,62,80]
print(f"最も低い点数：{min(scores)}")
print(f"最も高い点数：{max(scores)}")
print(f"合計点数：{sum(scores)}")
print(f"平均点：{sum(scores)/len(scores):.2f}")


scores.sort()
print(f"昇順に並べ替えた点数：{scores}")

scores.reverse()
print(f"降順に並べ替えた点数：{scores}")