# Lesson08 まとめ：継承（Inheritance）

## 今日のゴール

- 継承の考え方と、メリットを理解する
- 親クラスと子クラスを定義し、属性やメソッドを引き継げる
- 継承を活用して、共通部分をまとめたプログラムを作れる

---

# 1. 継承とは

## 継承がない場合の問題

`Player` と `Enemy` に、同じ属性・メソッドを重複して書いてしまう。

```text
・同じ処理を何度も書く
・仕様変更のとき、複数か所を直す必要がある
・直し忘れが起きる
・クラスが増えるほど管理が大変
```

## 継承の考え方

共通部分を **親クラス** にまとめ、**子クラス** から再利用する。

```text
          Character（親クラス）
          name / hp / show_status() / take_damage()
                  │
          ┌───────┴───────┐
        Player          Enemy
     （use_potion）     （growl）
```

| 用語 | 意味 |
| --- | --- |
| 親クラス（基底クラス） | 共通の属性・メソッドを提供する |
| 子クラス（派生クラス） | 親を引き継ぎ、独自の機能を追加する |

## is-a 関係

継承は「**○○は△△の一種**」と言える関係で使う。

```text
OK：プレイヤーはキャラクターの一種
OK：犬は動物の一種
NG：武器はキャラクターの一種 → 名前が共通でも継承しない
NG：戦闘（Battle）はキャラクターの一種 → 継承しない
```

> コードの共通点だけでなく、**クラス同士の関係が自然か**を考える。

## メリット

- コードの重複を減らせる
- 共通処理をまとめて変更できる（親を直せば子に反映）
- クラスの役割が分かりやすくなる
- 新しい種類のクラスを追加しやすい

---

# 2. Pythonでの継承

## 基本の書き方

```python
class 子クラス名(親クラス名):
    処理
```

```python
# 親クラス：キャラクター共通の機能
class Character:
    def __init__(self, name, hp):
        self.name = name    # 名前
        self.hp = hp        # 現在のHP
        self.max_hp = hp    # 最大HP（回復の上限に使う）

    # HPを表示する
    def show_status(self):
        print(f"{self.name}のHP：{self.hp}")

# 子クラス：Character を継承する（中身は何も書かない）
class Player(Character):
    pass

class Enemy(Character):
    pass
```

- 子クラスに `__init__()` がなければ、**親の `__init__()` がそのまま使われる**
- `pass` は「何も書かない」ときに使う

## 子クラス独自のメソッド

```python
class Player(Character):
    # ポーションを使う（プレイヤーだけの機能）
    def use_potion(self):
        self.heal(20)          # 親の heal() を呼べる
        print(f"{self.name}はポーションを使った！")

class Enemy(Character):
    # 威嚇する（敵だけの機能）
    def growl(self):
        print(f"{self.name}は威嚇している！")
```

| メソッド | Player | Enemy |
| --- | --- | --- |
| `show_status()` | ○ | ○ |
| `take_damage()` | ○ | ○ |
| `heal()` | ○ | ○ |
| `use_potion()` | ○ | × |
| `growl()` | × | ○ |

- 子クラスで使えるのは「**自分のクラス**」と「**親クラス**」のメソッド
- 兄弟クラスのメソッドは使えない → `slime.use_potion()` は `AttributeError`

## 属性の値はインスタンスごと

```python
hero.take_damage(30)   # 変わるのは hero のHPだけ（slime には影響しない）
```

親の仕組みを共有しても、**属性の値までは共有されない**。

---

# 3. `super()` と親のコンストラクタ

## 子クラスに `__init__()` を書くと

```text
子クラスに独自の __init__() を定義すると、
親の __init__() は自動では実行されない
```

## 重複した書き方（NG）

```python
class Player(Character):
    def __init__(self, name, hp, mp):
        self.name = name        # 親と同じ処理（重複）
        self.hp = hp            # 親と同じ処理（重複）
        self.max_hp = hp        # 親と同じ処理（重複）
        self.mp = mp            # プレイヤー独自の属性
```

→ 親に `level` を追加したら、親と子の両方を直す必要がある。

## `super().__init__()` を使う（OK）

```python
class Player(Character):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)   # 共通部分は親に任せる
        self.mp = mp                 # 独自の属性だけ自分で初期化

class Enemy(Character):
    def __init__(self, name, hp, reward_exp):
        super().__init__(name, hp)       # 共通部分は親に任せる
        self.reward_exp = reward_exp     # 敵独自の属性（獲得経験値）
```

### 初期化の流れ

```text
Player("勇者", 100, 30)
   ↓
Player の __init__()
   ↓
super().__init__(name, hp) → Character の __init__()
   （name / hp / max_hp を初期化）
   ↓
Player の __init__() に戻る
   ↓
mp = 30
```

## `super()` の注意点

```text
① 親のコンストラクタに必要な引数を渡す
② self は渡さない
     super().__init__(name, hp)          ← OK
     super().__init__(self, name, hp)    ← NG（エラー）
③ 先に super().__init__() を呼び、あとで子独自の属性を初期化する
   （親が作る属性を使う処理は、親の初期化より後に書く）
④ 子に独自の初期化が不要なら、__init__() は書かなくてよい
⑤ 一番上の親クラスには super().__init__() は書かない
```

---

# 4. 継承を活用したバトルプログラム

## 構成

```text
handson
├── main.py
├── character.py   ← 新規（共通部分）
├── player.py
├── enemy.py
└── battle.py      ← 変更しない
```

## `character.py`（親クラス）

```python
# 親クラス：Player と Enemy に共通する機能をまとめる
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name                    # 名前
        self.__hp = hp                      # 現在のHP（外から直接触らせない）
        self.__max_hp = hp                  # 最大HP
        self.__attack_power = attack_power  # 攻撃力

    # 相手を攻撃する
    def attack(self, target):
        print(f"{self.name}が{target.name}を攻撃！")
        target.take_damage(self.__attack_power)  # 相手にダメージを与える

    # ダメージを受ける
    def take_damage(self, amount):
        # 0以下のダメージは無効
        if amount <= 0:
            return

        self.__hp -= amount

        # HPは0未満にならない
        if self.__hp < 0:
            self.__hp = 0

        print(f"{self.name}は{amount}ダメージを受けた！")
        self.show_hp()

    # 現在のHPを表示する
    def show_hp(self):
        print(f"{self.name}のHP：{self.__hp}")

    # 生きているか判定する（HPが0より大きければ True）
    def is_alive(self):
        return self.__hp > 0

    # HPを回復する（子クラスから使うための内部用メソッド）
    # __hp はこのクラスの中でしか直接変更できないため、回復処理もここに用意する
    def _recover_hp(self, amount):
        if amount <= 0:
            return

        self.__hp += amount

        # 最大HPを超えない
        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp

        self.show_hp()
```

## なぜ `_recover_hp()` を親に用意するのか

```text
・__hp は名前マングリングで _Character__hp という名前になる
・子クラスの self.__hp は、親の __hp とは別物になる
・だから HP の値を変更する処理は、HP を持っている親（Character）に任せる
```

先頭の `_`（アンダースコア1つ）は「クラスの内部や関連クラスから使う想定」の目印。アクセスが禁止されるわけではない。

## 子クラス

```python
from character import Character  # 親クラスを読み込む

# 子クラス：プレイヤー固有の機能を追加する
class Player(Character):
    def __init__(self, name, hp, attack_power, mp):
        super().__init__(name, hp, attack_power)  # 共通部分は親に任せる
        self.mp = mp   # プレイヤー独自の属性：MP
        self.exp = 0   # プレイヤー独自の属性：経験値（最初は0）

    # HPを回復する（実際の処理は親の _recover_hp() に任せる）
    def heal(self, amount):
        self._recover_hp(amount)

    # ポーションを使う（HPが20回復する）
    def use_potion(self):
        print(f"{self.name}はポーションを使った！")
        self.heal(20)

    # MPを表示する
    def show_mp(self):
        print(f"{self.name}のMP：{self.mp}")

    # 経験値を獲得する
    def gain_exp(self, amount):
        if amount <= 0:
            return

        self.exp += amount
        print(f"{self.name}は{amount}の経験値を獲得した！")

    # 経験値を表示する
    def show_exp(self):
        print(f"{self.name}の経験値：{self.exp}")
```

```python
from character import Character  # 親クラスを読み込む

# 子クラス：敵固有の機能を追加する
class Enemy(Character):
    def __init__(self, name, hp, attack_power, reward_exp):
        super().__init__(name, hp, attack_power)  # 共通部分は親に任せる
        self.reward_exp = reward_exp  # 敵独自の属性：倒したときの獲得経験値

    # 獲得経験値を返す（ゲッター）
    def get_reward_exp(self):
        return self.reward_exp

    # 威嚇する
    def growl(self):
        print(f"{self.name}は威嚇している！")
```

## `Battle` は変更しなくていい

```text
Battle が呼ぶメソッド：attack() / show_hp() / is_alive()
→ すべて Character に定義され、Player と Enemy が継承している
→ 外から見た使い方が変わらないので、Battle は変更不要
```

> 内部のクラス構成を変えても、**外から使うメソッドの使い方を維持**できれば、既存のプログラムへの影響を抑えられる。

ただし、親のメソッド名や引数を変えた場合は、使っている側も直す必要がある。

## ゲッター（getter）

```python
# 値を取り出して返すメソッド（get_ + 属性名にするのが一般的）
def get_reward_exp(self):
    return self.reward_exp
```

- 値を取り出して返すメソッド。`get_` + 属性名にするのが一般的
- メソッド経由にすると、内部の作りを変えても使う側のコードを直さずに済む

---

# よくあるエラー

| エラー | 原因 | 直し方 |
| --- | --- | --- |
| `TypeError: Car() takes no arguments` | 子クラスが親を継承していない（`class Car:` のまま） | `class Car(Vehicle):` にする |
| `TypeError: ... missing 1 required positional argument` | 親の `__init__()` に渡す引数が足りない／親に子の引数が混ざっている | 親には共通の引数だけ書く |
| `AttributeError` | 親にも自分にも、そのメソッドがない | 定義されているクラスを確認する |
| `ModuleNotFoundError: No module named 'character'` | `character.py` が同じフォルダにない、またはファイル名が違う | 同じフォルダに小文字の `character.py` を置く |

---

# 確認問題の解答のポイント

## practice01：Vehicle / Car / Bicycle

```python
# 親クラス：乗り物に共通する機能
class Vehicle:
    def __init__(self, name, speed):
        self.name = name    # 乗り物の名前
        self.speed = speed  # 現在の速度

    # 名前と速度を表示する
    def show_status(self):
        print(f"{self.name}：{self.speed}km/h")

    # 加速する
    def accelerate(self, amount):
        # 0以下なら速度を変えない
        if amount <= 0:
            return

        self.speed += amount

# 子クラス：自動車（独自のコンストラクタなし → 親の __init__() を使う）
class Car(Vehicle):
    # クラクションを鳴らす
    def honk(self):
        print(f"{self.name}：プップー！")

# 子クラス：自転車
class Bicycle(Vehicle):
    # ベルを鳴らす
    def ring_bell(self):
        print(f"{self.name}：チリンチリン！")
```

- 独自のコンストラクタがなければ、親の `__init__()` がそのまま使われる

## practice02：Product / Book / Food

```python
# 子クラス：書籍
class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)  # 商品名と価格は親に任せる
        self.author = author           # 書籍独自の属性：著者

    # 著者名を表示する
    def show_author(self):
        print(f"著者：{self.author}")
```

- `super().__init__()` を先に呼び、そのあとで独自の属性を初期化する

## practice03：Animal / Dog / Bird

```python
from animal import Animal  # 親クラスを読み込む

# 子クラス：犬
class Dog(Animal):
    def __init__(self, name, energy, favorite_toy):
        super().__init__(name, energy)    # 名前と体力は親に任せる
        self.favorite_toy = favorite_toy  # 犬独自の属性：お気に入りのおもちゃ

    # 散歩する（体力を20消費）
    def walk(self):
        self.use_energy(20)  # 体力を減らす処理は親のメソッドを利用
        print(f"{self.name}は散歩した！")
```

- ファイルをまたぐときは、1行目に `from animal import Animal`
- 体力を減らす処理は、親の `use_energy()` を呼ぶ

---

# テスト頻出

## 問

```python
class Player(Character):
    pass
```

意味

```text
Player は Character を継承する子クラス
Character の属性とメソッドを引き継ぐ
```

---

## 問

```python
super().__init__(name, hp)
```

意味

```text
親クラスのコンストラクタを呼び出し、
共通の属性（name / hp など）を初期化する
```

---

## 問

子クラスに独自の `__init__()` を書くと、親の `__init__()` はどうなる？

```text
自動では実行されない
→ super().__init__() で明示的に呼ぶ
```

---

## 問

`Battle` が `Character` を継承しない理由

```text
Battle（戦闘）は Character（キャラクター）の一種ではないため
（is-a 関係が成り立たない）
```

---

# Lesson08 最重要まとめ

覚えることは4つ。

```text
① 共通部分は親クラスにまとめる
   class 子クラス(親クラス):

② 子クラスには独自の機能だけを追加する

③ 子クラスの __init__() では super().__init__() で親に初期化を任せる
   （self は渡さない）

④ 継承は「○○は△△の一種」のときに使う
   → 目的は、コードを短くすることではなく、分かりやすく管理すること
```