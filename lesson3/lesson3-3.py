

def local_scope_function():
    message="これはローカル変数です"
    print(f"ローカル変数messageの値: {message}")
    
greeting="こんにちは"
def greet():
    print(f"グローバル変数greetingの値： {greeting}")
    
def modify_global_variable():
    global greeting
    greeting="こんにちは、世界！"
    print(f"グローバル変数greetingが関数内で変更されました: {greeting}")


local_scope_function()
greet()
modify_global_variable()
print(f"関数外のグローバル変数greetingの値: {greeting}")
    
