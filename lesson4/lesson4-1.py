# リストに使うメソッド
my_list=[1,2,4]
print(my_list)
my_list.append(5) # 末尾に追加
print(my_list)
my_list.extend([6,7]) # 末尾に複数追加
print(my_list)
my_list.insert(3,3) # 指定した位置に追加
print(my_list)
my_list.remove(4) # 指定した値を削除
print(my_list)
my_list.pop() # 末尾の値を削除
print(my_list)
my_list.pop(0) # 指定した位置の値を削除
print(my_list)
print(my_list.index(5)) # 指定した値の位置を取得
print(my_list.count(2)) # 指定した値の個数を取得
my_list.sort() # 昇順にソート
print(my_list)
my_list.sort(reverse=True) # 降順にソート
print(my_list)
my_list.reverse() # 逆順に並び替え
print(my_list)
print(len(my_list)) # リストの長さを取得
my_list.clear() # リストの中身を空にする
print(my_list)
