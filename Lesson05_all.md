# Lesson05 カプセル化まとめ

## 本日のゴール

- カプセル化の考え方を理解する
- 属性を直接変更されにくくする
- メソッド経由で安全にデータを操作する
- 内部の仕組みを意識せず利用できるプログラムを作る

---

# カプセル化とは

## 一言でいうと

**データ（属性）と処理（メソッド）をまとめて、安全に管理する考え方**

---

## カプセル化が必要な理由

### 悪い例

```python
hero.hp = -500
```

結果

```text
勇者のHP：-500
```

---

### こんな問題が起きる

```python
hero.hp = -500
hero.hp = 999999
```

- HPがマイナスになる
- HPが異常に大きくなる
- ゲームのルールが壊れる

---

# カプセル化のメリット

## ① データを安全に管理できる

```python
hero.take_damage(30)
```

↓

```python
HPが0未満にならない
```

---

## ② 内部の仕組みを隠せる

利用者は

```python
hero.attack(slime)
```

だけ知っていればよい。

---

## ③ 修正しやすい

内部のダメージ計算を変更しても

```python
hero.attack(slime)
```

は変更不要。

---

# カプセル化の考え方

## 外部から

```python
hero.attack(slime)
```

だけ使う

---

## 内部で

```python
damage = 複雑な計算

target.take_damage(damage)
```

を実行する

---

# __ を使った属性保護

## 普通の属性

```python
self.hp = hp
```

外部から変更可能

```python
hero.hp = -500
```

---

## 保護する属性

```python
self.__hp = hp
```

```python
self.__max_hp = hp
```

---

## アクセス確認

```python
print(hero.__hp)
```

結果

```text
AttributeError
```

---

# 名前マングリング

```python
self.__hp
```

↓

内部では

```python
_Character__hp
```

として管理される

---

## ポイント

完全に隠れるわけではない。

Pythonでは

```text
この変数は直接触らないでください
```

という意味で使う。

---

# HP管理の改良

## __init__()

```python
def __init__(self, name, hp, attack_power):

    self.name = name

    self.__hp = hp
    self.__max_hp = hp

    self.attack_power = attack_power
```

---

# take_damage()

## HPを減らす

```python
def take_damage(self, amount):

    if amount <= 0:
        return

    self.__hp -= amount

    if self.__hp < 0:
        self.__hp = 0
```

---

## 不正なダメージを防ぐ

```python
slime.take_damage(-20)
```

結果

```text
ダメージ量は1以上で指定してください。
```

---

# heal()

## HP回復

```python
def heal(self, amount):
```

---

## 回復量チェック

```python
if amount <= 0:
    return
```

---

## 最大HP制限

```python
if self.__hp > self.__max_hp:
    self.__hp = self.__max_hp
```

---

## 例

```python
HP = 70
MAX = 100

heal(50)
```

本来

```python
70 + 50 = 120
```

だが

```python
100
```

になる。

---

# is_alive()

## 生存確認

```python
def is_alive(self):
    return self.__hp > 0
```

---

## 使用例

変更前

```python
while hero.hp > 0:
```

---

変更後

```python
while hero.is_alive():
```

---

## メリット

外部は

```text
生きているか
```

だけ分かればよい。

HPの管理方法を知らなくてよい。

---

# get_hp()

## HP取得

```python
def get_hp(self):
    return self.__hp
```

---

## 使用例

```python
print(hero.get_hp())
```

---

# ゲッターとセッター

## ゲッター

値を取得するメソッド

```python
def get_hp(self):
    return self.__hp
```

---

## 使用例

```python
hp = hero.get_hp()
```

---

## セッター

値を設定するメソッド

```python
def set_hp(self, hp):

    if 0 <= hp <= self.__max_hp:
        self.__hp = hp
```

---

## ただし

今回は

```python
set_hp()
```

より

```python
take_damage()
heal()
```

の方が自然

---

### 理由

```python
hero.set_hp(10)
```

より

```python
hero.take_damage(90)
```

の方が意味が分かりやすい。

---

# HP関連メソッド一覧

| メソッド | 役割 |
|-----------|-----------|
| take_damage() | HP減少 |
| heal() | HP回復 |
| get_hp() | HP取得 |
| show_hp() | HP表示 |
| is_alive() | 生存判定 |

---

# ダメージ計算のカプセル化

## 単純版

```python
damage = attack_power
```

---

## 複雑版

```python
damage = (
    (attack_power ** 3 / 32 + 30)
    * (...)
)
```

---

## 重要

外部コードは変わらない

```python
hero.attack(slime)
```

---

### 内部だけ変更

```python
def attack(self, target):
```

の中だけ修正

---

# attack()の役割

```python
hero.attack(slime)
```

↓

```python
ダメージ計算
```

↓

```python
slime.take_damage(damage)
```

---

# defense取得

## ゲッターを使う

```python
def get_defense(self):
    return self.__defense
```

---

## 使用例

```python
defense = target.get_defense()
```

---

# カプセル化で大切なこと

## NG

```python
hero.__hp = -500
```

```python
hero.hp = -500
```

---

## OK

```python
hero.take_damage(30)
```

```python
hero.heal(20)
```

```python
hero.get_hp()
```

```python
hero.is_alive()
```

---

# オブジェクト指向的な考え方

## データ

```python
__hp
__max_hp
__attack_power
__defense
```

---

## 操作

```python
take_damage()
heal()
attack()
```

---

## 役割分担

```text
attack()
↓
攻撃する

take_damage()
↓
HPを減らす

heal()
↓
HPを回復する

is_alive()
↓
生存判定
```

---

# 試験対策

## Q. カプセル化とは？

データと処理をクラスにまとめ、
安全に管理する考え方。

---

## Q. __hp の意味は？

外部から直接アクセスされにくくする属性。

---

## Q. ゲッターとは？

値を取得するメソッド。

例

```python
get_hp()
```

---

## Q. セッターとは？

値を設定するメソッド。

例

```python
set_hp()
```

---

## Q. HP確認はどうする？

```python
hero.get_hp()
```

---

## Q. 生存確認は？

```python
hero.is_alive()
```

---

## Q. HP回復は？

```python
hero.heal(20)
```

---

## Q. HP減少は？

```python
hero.take_damage(30)
```

---

## Q. attack()の役割は？

ダメージを計算して相手へ与える。

```python
target.take_damage(damage)
```

---

# 超重要まとめ

✅ カプセル化 = データと処理をまとめて管理する

✅ `__hp` のように `__` を付けると外部から触りにくくなる

✅ HP変更は属性を直接触らずメソッドで行う

```python
take_damage()
heal()
```

✅ 値取得はゲッター

```python
get_hp()
```

✅ 状態確認は専用メソッド

```python
is_alive()
```

✅ 内部の処理を変えても

```python
hero.attack(slime)
```

の使い方は変わらない

✅ 「何をするか」と「どうやるか」を分けるのがカプセル化