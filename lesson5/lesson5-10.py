# ミックスイン
# 文法的な違いは普通のクラスと変わらない。しかし、部品だけの設計を前提としていたり、慣習でMixinがついたりなどの違いがある。

class LogginMixin:
    def log(self, message):
        print("[LOG]：",message)
        
class ValidationMixin:
    def validate_input(self, data):
        if isinstance(data, str):
            print("入力は有効です。")
            return True
        else:
            print("入力は無効です。")
            return False

class UserProcessor(LogginMixin, ValidationMixin):
    def process_user(self, username):
        if self.validate_input(username):
            self.log(f"ユーザー名'{username}'を正常に処理しました。")
        else:
            self.log("処理に失敗しました。")
            
process=UserProcessor()
username=input("ユーザー名を入力してください。：")
process.process_user(username)