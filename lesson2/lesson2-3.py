tenki=input("今日の天気は 晴れ or 雨 or 曇り？")
if tenki == "晴れ":
    print("外出しましょう")
elif tenki == "雨":
    print("家にいましょう")
elif tenki == "曇り":
    print("軽く散歩でもしましょう")
else:
    print("指定された天気ではありません")