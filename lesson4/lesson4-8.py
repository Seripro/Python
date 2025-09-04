# リストを使って、順序を持ち変更可能なフルーツのリストを作成
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')  # 'orange'を追加
fruits.remove('apple')   # 'apple'を削除
print("リスト:", fruits)  # 出力: ['banana', 'cherry', 'orange']

# タプルを使って、変更できない（immutable）要素を作成
number = (100, 200)
# number[0] = 300  ← この部分をコメントではなくすとエラーが発生します
print("タプル:", number)  # 出力: (100, 200)

# 辞書を使って、名前や年齢などの個人情報をキーを使って管理
person = {'name': 'Alice', 'age': 30, 'city': 'Tokyo'}
print("辞書:", person['name'])  # 出力: 'Alice'

# 集合を使って、AグループとBグループの両方に属している人を表示
A_group = {'太郎', '次郎', '三郎'}
B_group = {'太郎', '三郎', '四郎'}
common_members = A_group & B_group  # AとBの両方に属している人（積集合）
print("集合（両方のグループに属している人）:", common_members)  # 出力: {'太郎', '三郎'}