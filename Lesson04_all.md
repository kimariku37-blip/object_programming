# Lesson04 インスタンス同士のやり取り まとめ

## 本日のゴール

- インスタンスを引数として渡し、別のインスタンスを操作できる
- 複数のインスタンスが連携するプログラムを実装できる
- クラス・属性・メソッドを活用して、さまざまなプログラムを作成できる

---

# 1. インスタンス同士のやり取り

## インスタンスを引数に渡せる

数値や文字列だけでなく、インスタンスも引数として渡せる。

```python
hero.greet(wizard)
```

---

## 例

```python
class Character:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def greet(self, target):
        print(f"{self.name}は{target.name}にあいさつした")
```

```python
hero = Character("勇者", 100)
wizard = Character("魔法使い", 70)

hero.greet(wizard)
```

実行結果

```text
勇者は魔法使いにあいさつした
```

---

## 対応関係

```python
hero.greet(wizard)
```

```text
self   → hero
target → wizard
```

---

# 2. 別のインスタンスの属性を変更する

## HP回復

```python
def support(self, target, amount):
    target.hp += amount
```

---

## 使用例

```python
hero.support(wizard, 20)
```

```text
self   → hero
target → wizard
amount → 20
```

結果

```python
wizard.hp += 20
```

---

# 3. 別のインスタンスのメソッドを呼び出す

## heal()を作る

```python
def heal(self, amount):
    self.hp += amount
```

---

## support()から呼ぶ

```python
def support(self, target, amount):
    target.heal(amount)

    print(
        f"{self.name}は{target.name}のHPを{amount}回復させた"
    )
```

---

## 使用例

```python
wizard.support(hero, 10)
```

流れ

```text
wizard.support(hero,10)
        ↓
hero.heal(10)
        ↓
hero.hpが10増加
```

---

# 4. selfの変化

## support()の中

```text
self   → wizard
target → hero
```

---

## heal()の中

```text
self → hero
```

---

### ポイント

selfは固定ではない。

**メソッドを呼び出したインスタンス自身になる。**

---

# 5. バトルプログラム

## Characterクラス

```python
class Character:

    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
```

---

## HP表示

```python
def show_hp(self):
    print(f"{self.name}のHP：{self.hp}")
```

---

## 攻撃

```python
def attack(self, target):
    print(f"{self.name}が{target.name}を攻撃！")

    target.take_damage(
        self.attack_power
    )
```

---

## ダメージ処理

```python
def take_damage(self, amount):

    self.hp -= amount

    if self.hp < 0:
        self.hp = 0

    print(
        f"{self.name}は{amount}ダメージを受けた！"
    )

    self.show_hp()
```

---

# 6. attack()とtake_damage()

## attack()

```python
hero.attack(slime)
```

---

### attackの中

```text
self   → hero
target → slime
```

```python
target.take_damage(
    self.attack_power
)
```

↓

```python
slime.take_damage(25)
```

---

### take_damageの中

```text
self   → slime
amount → 25
```

```python
self.hp -= amount
```

↓

```python
slime.hp -= 25
```

---

# 7. while文で戦闘

```python
while hero.hp > 0 and slime.hp > 0:

    hero.attack(slime)

    if slime.hp <= 0:
        break

    slime.attack(hero)
```

---

## 意味

```text
勇者が攻撃
    ↓
スライム生存？
    ↓
YES
    ↓
スライム反撃
    ↓
繰り返し
```

---

# 8. 勝敗判定

```python
if slime.hp == 0:
    print("スライムを倒した！")
else:
    print("勇者は倒れてしまった...")
```

---

# 9. 完成コード

```python
class Character:

    def __init__(
        self,
        name,
        hp,
        attack_power
    ):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def show_hp(self):
        print(
            f"{self.name}のHP：{self.hp}"
        )

    def attack(self, target):
        print(
            f"{self.name}が{target.name}を攻撃！"
        )

        target.take_damage(
            self.attack_power
        )

    def take_damage(self, amount):

        self.hp -= amount

        if self.hp < 0:
            self.hp = 0

        print(
            f"{self.name}は{amount}ダメージを受けた！"
        )

        self.show_hp()


hero = Character(
    "勇者",
    100,
    25
)

slime = Character(
    "スライム",
    60,
    15
)

print("===== バトル開始！ =====")

hero.show_hp()
slime.show_hp()

while hero.hp > 0 and slime.hp > 0:

    print()

    hero.attack(slime)

    if slime.hp <= 0:
        break

    print()

    slime.attack(hero)

print()

if slime.hp == 0:
    print("スライムを倒した！")
else:
    print("勇者は倒れてしまった...。")

print("===== バトル終了 =====")
```

---

# 試験・小テスト対策

## Q. インスタンスを引数に渡せる？

渡せる。

```python
hero.attack(slime)
```

---

## Q. targetとは？

引数で受け取った別のインスタンス。

---

## Q. selfとは？

メソッドを呼び出したインスタンス自身。

---

## Q. 別のインスタンスのメソッドを呼ぶには？

```python
target.heal(20)
```

---

## Q. attack()の役割は？

相手を攻撃する。

```python
target.take_damage(
    self.attack_power
)
```

---

## Q. take_damage()の役割は？

自分自身のHPを減らす。

```python
self.hp -= amount
```

---

## Q. HPがマイナスにならないようにするには？

```python
if self.hp < 0:
    self.hp = 0
```

---

# よく出る対応関係

## hero.attack(slime)

```text
self   → hero
target → slime
```

---

## slime.take_damage(25)

```text
self   → slime
amount → 25
```

---

## wizard.support(hero, 10)

```text
self   → wizard
target → hero
amount → 10
```

---

# オブジェクト指向の考え方

## 悪い例

```python
target.hp -= amount
```

すべての処理を外から変更する。

---

## 良い例

```python
target.take_damage(amount)
```

ダメージ処理は相手自身に任せる。

---

### 役割分担

```text
attack()
↓
攻撃する

take_damage()
↓
ダメージ処理

show_hp()
↓
HP表示
```

---

# 一言まとめ

- インスタンスは引数として渡せる
- selfは自分自身、targetは相手
- 別のインスタンスの属性やメソッドを利用できる
- attack() → take_damage() のようにインスタンス同士で連携できる
- オブジェクト指向では「誰がその処理を担当するか」を考えることが大切
- クラス同士のやり取りができると、本格的なゲームやシステムを作れる