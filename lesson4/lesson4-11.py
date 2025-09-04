# 辞書の基本 難しかった。
inventory={
    'りんご':{'価格':100, '在庫数':50},
    'バナナ':{'価格':80, '在庫数':30},
    'みかん':{'価格':60,'在庫数':100}
}

print("初期の在庫：",inventory)

inventory['ぶどう']={'価格':120, '在庫数':25}
print("ぶどうを追加した後の在庫：",inventory)

inventory['りんご']['在庫数']=40
print("りんごの在庫数を更新した後の在庫：",inventory)
del inventory['バナナ']
print("バナナを削除した後の在庫：",inventory)

for fruit, info in inventory.items():
    print(f"{fruit}：価格 = {info['価格']}円, 在庫数 = {info['在庫数']}個")



