# Lesson02 クラスとインスタンス（属性編）まとめ

## 本日のゴール

- Pythonでクラスを定義し、複数のインスタンスを作成できる
- インスタンスに属性を持たせ、値の参照や変更ができる
- インスタンスをリストや関数と組み合わせて扱うことができる

---

# 1. クラスとインスタンスの復習

## クラスとは

クラスはオブジェクトを作るための設計図（ひな形）。

```python
class Player:
    pass
```

### ポイント

- `class` で定義する
- クラス名は先頭を大文字にする
- `pass` は何もしないという意味

---

## インスタンスとは

クラスから実際に作られたオブジェクトのこと。

```python
player = Player()
```

### イメージ

```text
Playerクラス
     ↓
 Player()
     ↓
 player
```

---

# 2. 属性（Attribute）

## 属性とは

オブジェクトが持つデータ。

例

- 名前
- HP
- レベル

---

## 属性を設定する

```python
class Player:
    pass

player = Player()

player.name = "勇者"
player.hp = 100
player.level = 1
```

### 基本形

```python
インスタンス.属性名 = 値
```

---

## 属性を参照する

```python
print(player.name)
print(player.hp)
print(player.level)
```

### 実行結果

```text
勇者
100
1
```

---

## 属性を変更する

### HPを減らす

```python
player.hp -= 20
```

または

```python
player.hp = player.hp - 20
```

### レベルアップ

```python
player.level += 1
```

---

# 3. 複数のインスタンス

## 同じクラスから複数作れる

```python
player1 = Player()
player2 = Player()
```

---

## 別々のデータを持たせる

```python
player1.name = "勇者"
player1.hp = 100

player2.name = "魔法使い"
player2.hp = 80
```

### 状態

```text
player1
├ 名前：勇者
└ HP：100

player2
├ 名前：魔法使い
└ HP：80
```

---

## インスタンスは独立している

```python
player1.hp -= 30
```

結果

```text
勇者 HP：70
魔法使い HP：80
```

player1だけ変化する。

---

# 4. リストで管理する

## インスタンスをリストに入れる

```python
players = [player1, player2, player3]
```

### イメージ

```text
players
├ player1
├ player2
└ player3
```

---

## for文で取り出す

```python
for player in players:
    print(player.name)
```

### 実行結果

```text
勇者
魔法使い
戦士
```

---

## 属性も使える

```python
for player in players:
    print(player.name)
    print(player.hp)
```

### 実行結果

```text
勇者
100

魔法使い
80

戦士
150
```

---

# 5. 関数にインスタンスを渡す

## プレイヤー情報を表示

```python
def show_player(player):
    print(player.name)
    print(player.hp)
    print(player.level)
```

呼び出し

```python
show_player(player1)
```

---

## 関数で属性を変更

```python
def damage_player(player, damage):
    player.hp -= damage
```

呼び出し

```python
damage_player(player1, 30)
```

結果

```text
100 → 70
```

---

# 6. リスト・for文・関数の組み合わせ

```python
for player in players:
    show_player(player)
```

### 処理の流れ

```text
players
 ↓
for文
 ↓
player
 ↓
show_player(player)
 ↓
属性を表示
```

---

# 7. アイテムショップで学んだこと

## Itemクラス

```python
class Item:
    pass
```

---

## 商品作成

```python
item1 = Item()

item1.name = "薬草"
item1.price = 50
item1.stock = 10
```

---

## リストにまとめる

```python
items = [item1, item2, item3]
```

---

## 商品一覧表示

```python
def show_items(items):
    for item in items:
        print(item.name)
        print(item.price)
        print(item.stock)
```

---

## 商品購入

```python
def purchase_item(item):
    item.stock -= 1
```

呼び出し

```python
purchase_item(items[1])
```

---

# 試験・小テスト対策

## Q. クラスとは？

オブジェクトを作るための設計図。

---

## Q. インスタンスとは？

クラスから実際に作られたオブジェクト。

---

## Q. 属性とは？

インスタンスが持つデータ。

例

- name
- hp
- level

---

## Q. 属性を設定する書き方は？

```python
player.name = "勇者"
```

---

## Q. 属性を参照する書き方は？

```python
print(player.name)
```

---

## Q. 属性を変更する書き方は？

```python
player.hp -= 20
```

---

## Q. インスタンスをリストに入れられる？

入れられる。

```python
players = [player1, player2, player3]
```

---

## Q. インスタンスを関数に渡せる？

渡せる。

```python
show_player(player)
```

---

# 覚えるコード一覧

## クラス作成

```python
class Player:
    pass
```

## インスタンス作成

```python
player = Player()
```

## 属性設定

```python
player.name = "勇者"
player.hp = 100
player.level = 1
```

## 属性参照

```python
print(player.name)
```

## 属性変更

```python
player.hp -= 20
```

## リスト化

```python
players = [player1, player2, player3]
```

## for文

```python
for player in players:
    print(player.name)
```

## 関数

```python
def show_player(player):
    print(player.name)
```

## ダメージ関数

```python
def damage_player(player, damage):
    player.hp -= damage
```

## リストから取得

```python
players[0]
players[1]
players[2]
```

```python
selected_index = 1
player = players[selected_index]
```

---

# 一言まとめ

- クラス = 設計図
- インスタンス = 実体
- 属性 = オブジェクトが持つデータ
- インスタンスはリストに入れたり関数へ渡したりできる
- 属性は参照・変更できる
- リスト + for文 + 関数 と組み合わせると大量のオブジェクトを効率よく扱える