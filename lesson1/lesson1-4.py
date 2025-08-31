#文字列について

text="Hello World World"
#部分文字列の抽出
greeting=text[0:5]
print(greeting)

#文字列の置換
new_text=text.replace("World","Japan")
print(new_text)

#文字列に特定の単語が含まれているかをチェック
check="Hello" in text
print(check)

#大文字、小文字
print("hello".upper())
print("heLlO".lower())

#前方一致、後方一致の確認
start=text.startswith("Hello")
end=text.endswith("World")
print(start,"\n",end) #改行　ただし、カンマを使うと出力されるときにendの前にスペースができる
print(f"{start}\n{end}") #改行　endの前にスペースができるやつの対策




