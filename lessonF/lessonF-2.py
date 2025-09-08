import time

def greeting_logger(func):
    def wrapper(): # この内部関数は必要。最初これを省略して、デコレーター関数に直接書いてたんだけど、なにか関数をreturnしないとエラーになるらしい。
        print("=== 処理を開始します ===")
        start=time.time()
        func()
        end=time.time()
        print("=== 処理が終了しました ===")
        print(f"実行時間：{end-start:.2f}秒")
    return wrapper
    
@greeting_logger
def greet_user():
    name=input("あなたの名前を入力してください：")
    print(f"こんにちは、{name}さん！ようこそ！")
    
greet_user()