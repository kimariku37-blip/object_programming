# Lesson03 メソッド・self・__init__ まとめ

## 本日のゴール

- クラスにメソッドを定義し、インスタンスから呼び出せる
- `self` を使ってインスタンスの属性を参照・変更できる
- `__init__()` を使ってインスタンス生成時に属性を初期化できる

---

# 1. メソッド

## メソッドとは

クラスの中に定義された関数のこと。

```python
class Character:
    def greet(self):
        print("こんにちは")
```

---

## メソッドの呼び出し

```python
character = Character()

character.greet()
```

実行結果

```text
こんにちは
```

---

## 関数との違い

### 関数

```python
show_status(hero)
```

### メソッド

```python
hero.show_status()
```

---

### イメージ

```text
関数
↓
show_status(hero)

メソッド
↓
hero.show_status()
```

メソッドは

> オブジェクト自身が処理を行う

という考え方になる。

---

# 2. self

## selfとは

メソッドを呼び出したインスタンス自身を表す。

```python
class Character:
    def show_name(self):
        print(self.name)
```

---

## 例

```python
hero = Character()

hero.name = "勇者"

hero.show_name()
```

実行結果

```text
勇者
```

このとき

```python
self
```

は

```python
hero
```

を表している。

---

## イメージ

```text
hero.show_name()

↓

self = hero
```

---

# 3. selfで属性を参照する

```python
class Character:
    def show_status(self):
        print(self.name)
        print(self.hp)
```

---

## 使用例

```python
hero = Character()

hero.name = "勇者"
hero.hp = 100

hero.show_status()
```

実行結果

```text
勇者
100
```

---

# 4. selfで属性を変更する

```python
class Character:
    def heal(self):
        self.hp += 10
```

---

## 使用例

```python
hero = Character()

hero.hp = 100

hero.heal()

print(hero.hp)
```

実行結果

```text
110
```

---

# 5. メソッドに引数を渡す

## 回復量を指定する

```python
class Character:
    def heal(self, amount):
        self.hp += amount
```

---

## 使用例

```python
hero = Character()

hero.hp = 100

hero.heal(30)

print(hero.hp)
```

実行結果

```text
130
```

---

## 対応関係

```python
hero.heal(30)

self   → hero
amount → 30
```

---

## 注意

呼び出すときに self は書かない

❌

```python
hero.heal(hero, 30)
```

✅

```python
hero.heal(30)
```

---

# 6. メソッドの戻り値

メソッドでも return が使える。

```python
class Product:
    def get_half_price(self):
        return self.price / 2
```

---

## 使用例

```python
product = Product()

product.price = 2000

half_price = product.get_half_price()

print(half_price)
```

実行結果

```text
1000.0
```

---

# 7. selfから別のメソッドを呼ぶ

```python
class Character:

    def show_hp(self):
        print(self.hp)

    def heal(self, amount):
        self.hp += amount
        self.show_hp()
```

---

## 使用例

```python
hero = Character()

hero.hp = 100

hero.heal(30)
```

実行結果

```text
130
```

---

# 8. __init__()

## __init__とは

インスタンス生成時に自動実行される特殊なメソッド。

```python
class Character:

    def __init__(self):
        print("初期化されました")
```

---

## 使用例

```python
hero = Character()
```

実行結果

```text
初期化されました
```

---

# 9. __init__で属性を初期化する

## 今まで

```python
hero = Character()

hero.name = "勇者"
hero.hp = 100
hero.level = 5
```

---

## __init__使用後

```python
class Character:

    def __init__(self):
        self.name = "勇者"
        self.hp = 100
        self.level = 5
```

---

## 使用例

```python
hero = Character()

print(hero.name)
print(hero.hp)
```

実行結果

```text
勇者
100
```

---

# 10. __init__に引数を渡す

```python
class Character:

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
```

---

## インスタンス作成

```python
hero = Character("勇者", 100, 5)

wizard = Character("魔法使い", 70, 4)

warrior = Character("戦士", 130, 6)
```

---

### 対応関係

```python
hero = Character("勇者", 100, 5)

self  → hero
name  → "勇者"
hp    → 100
level → 5
```

---

# 11. __init__と通常メソッドの違い

## __init__()

```python
def __init__(self):
```

- インスタンス生成時に自動実行
- 初期値を設定する

---

## 通常メソッド

```python
def show_status(self):
```

- 必要なときに自分で呼び出す
- 処理を実行する

---

# 12. 属性とメソッドをまとめる

```python
class Character:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def heal(self, amount):
        self.hp += amount

    def show_status(self):
        print(self.name)
        print(self.hp)
```

---

## イメージ

```text
Character
├ name
├ hp
├ heal()
└ show_status()
```

---

# 試験・小テスト対策

## Q. メソッドとは？

クラスの中に定義された関数。

---

## Q. selfとは？

メソッドを呼び出したインスタンス自身。

---

## Q. selfを使う理由は？

インスタンスの属性やメソッドを利用するため。

---

## Q. メソッドで属性を参照するには？

```python
self.name
self.hp
```

---

## Q. メソッドで属性を変更するには？

```python
self.hp += 10
```

---

## Q. __init__とは？

インスタンス生成時に自動で呼ばれる初期化メソッド。

---

## Q. __init__の目的は？

属性の初期値を設定すること。

---

## Q. selfは呼び出し時に書く？

書かない。

✅

```python
hero.heal(30)
```

❌

```python
hero.heal(hero, 30)
```

---

# 覚えるコード一覧

## メソッド

```python
class Character:

    def greet(self):
        print("こんにちは")
```

---

## self

```python
self.name
self.hp
```

---

## 属性変更

```python
self.hp += 10
```

---

## メソッド引数

```python
def heal(self, amount):
    self.hp += amount
```

---

## 戻り値

```python
def get_half_price(self):
    return self.price / 2
```

---

## __init__

```python
def __init__(self, name, hp):
    self.name = name
    self.hp = hp
```

---

## インスタンス生成

```python
hero = Character("勇者", 100)
```

---

# 一言まとめ

- メソッド = クラスの中の関数
- self = メソッドを呼び出したインスタンス自身
- selfで属性の参照・変更ができる
- メソッドにも引数・戻り値がある
- __init__ = インスタンス生成時の初期化
- オブジェクト指向では「データ(属性)」と「処理(メソッド)」を同じクラスにまとめる