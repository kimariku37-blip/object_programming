# Lesson06 まとめ

## 学習目標

- クラスごとに責任を分ける
- インスタンスをクラスへ渡す
- ファイル分割を行う
- importを使って別ファイルのクラスを利用する
- 複数クラスで協力してプログラムを作る

---

# 1. クラスの責任

責任（Responsibility）とは

```text
クラスが担当する仕事
```

---

## Characterクラス

```python
class Character:
```

担当

```text
HP管理
攻撃
ダメージ
生存判定
```

---

### attack()

```python
def attack(self, target):
```

相手を攻撃する

---

### take_damage()

```python
def take_damage(self, amount):
```

ダメージを受ける

---

### is_alive()

```python
def is_alive(self):
```

生きているか判定

---

# 2. クラスを分ける

## Player

担当

```text
HP管理
攻撃
回復
ダメージ
生存判定
```

---

## Enemy

担当

```text
HP管理
攻撃
ダメージ
生存判定
```

---

## Battle

担当

```text
戦闘開始
戦闘進行
勝敗判定
戦闘終了
```

---

## クラスを分けるメリット

### ① 理解しやすい

どこに何があるか分かる

---

### ② 修正しやすい

修正箇所が分かりやすい

---

### ③ 再利用しやすい

別のプログラムでも使える

---

# 3. インスタンスを渡す

## Battleのコンストラクタ

```python
class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
```

---

## 呼び出し

```python
hero = Player("勇者", 100, 25)
slime = Enemy("スライム", 60, 15)

battle = Battle(hero, slime)
```

---

### 結果

```text
self.player → hero
self.enemy → slime
```

---

# 4. Battleクラス

## show_status()

```python
battle.show_status()
```

表示

```text
===== 戦闘参加者 =====
勇者のHP：100
スライムのHP：60
```

---

## one_turn()

```python
battle.one_turn()
```

処理

```text
勇者攻撃
↓
敵生存確認
↓
敵反撃
```

---

## start()

```python
battle.start()
```

処理

```text
戦闘開始
↓
HP表示
↓
戦闘ループ
↓
勝敗判定
↓
戦闘終了
```

---

## 勝敗判定

```python
def show_result(self):
```

担当

```text
Battle
```

---

理由

```text
戦闘全体の結果を管理するため
```

---

# 5. while文

## 重要

```python
while self.player.is_alive() and self.enemy.is_alive():
```

意味

```text
プレイヤーと敵の両方が生きている間
戦闘を繰り返す
```

---

# 6. ファイル分割

## 分割前

```text
main.py
```

に全部書く

---

## 分割後

```text
handson
├── main.py
├── player.py
├── enemy.py
└── battle.py
```

---

## 各ファイルの役割

### main.py

```text
インスタンス生成
プログラム開始
```

---

### player.py

```text
Playerクラス
```

---

### enemy.py

```text
Enemyクラス
```

---

### battle.py

```text
Battleクラス
```

---

# 7. import

## Playerを読み込む

```python
from player import Player
```

---

## Enemyを読み込む

```python
from enemy import Enemy
```

---

## Battleを読み込む

```python
from battle import Battle
```

---

## NG

```python
from player.py import Player
```

---

## OK

```python
from player import Player
```

---

# 8. よくあるエラー

## ModuleNotFoundError

意味

```text
ファイルが見つからない
```

---

原因

```text
保存場所が違う
```

---

## ImportError

意味

```text
クラスが見つからない
```

---

原因

```text
player.pyの中に
Playerクラスがない
```

---

## NameError

意味

```text
定義されていない
```

---

原因

```python
import忘れ
```

---

# practice01 自動販売機

## Drink

担当

```text
商品情報
在庫管理
```

---

## VendingMachine

担当

```text
購入処理
```

---

### 重要

NG

```python
self.drink.__stock -= 1
```

OK

```python
self.drink.sell_one()
```

---

# practice02 社員管理

## Employee

担当

```text
社員情報管理
```

---

## Department

担当

```text
社員一覧管理
```

---

### 重要

```python
department.add_employee(employee)
```

---

# practice03 ゲーム大会

## Contestant

担当

```text
得点管理
```

---

属性

```python
self.__score
```

---

メソッド

```python
add_score()
get_score()
show_score()
```

---

## Tournament

担当

```text
大会進行
ラウンド管理
優勝判定
```

---

メソッド

```python
play_round()
show_result()
start()
```

---

### 重要

NG

```python
self.player1.__score += 20
```

OK

```python
self.player1.add_score(20)
```

---

# テスト頻出

## 問

```python
self.player = player
```

意味

```text
受け取ったplayerインスタンスを
self.playerへ保存する
```

---

## 問

```python
battle = Battle(hero, slime)
```

意味

```text
heroとslimeを渡して
Battleインスタンスを作成する
```

---

## 問

```python
from player import Player
```

意味

```text
player.pyのPlayerクラスを利用する
```

---

## 問

```python
while self.player.is_alive() and self.enemy.is_alive():
```

意味

```text
プレイヤーと敵が両方生存している間
繰り返す
```

---

# Lesson06 最重要まとめ

覚えることは4つ。

```text
① 責任を分ける

② インスタンスを渡す

③ ファイルを分割する

④ importで読み込む
```