animal=input("動物の名前を入力してください（犬/猫/鳥）:")
match animal:
    case "犬":
        print("ワンワン")
    case "猫":
        print("ニャーニャー")
    case "鳥":
        print("ピーピー")
    case _:
        print("その動物は記録されていません")