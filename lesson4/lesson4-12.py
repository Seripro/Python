# 辞書のキーと値の取得
student_scores={
    "山田":85,
    "佐藤":92,
    "鈴木":78,
}

print("学生の名前一覧：")
for name in student_scores.keys():
    print(name)
    
print("学生のスコア一覧：")
for score in student_scores.values():
    print(score)
    
print("学生の名前とスコア：")
for name, score in student_scores.items():
    print(f"{name}のスコアは{score}点です。")