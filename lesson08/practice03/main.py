from dog import Dog
from bird import Bird


dog = Dog("ポチ", 80, "ボール")
bird = Bird("ピーちゃん", 50, 30)

dog.show_status()
bird.show_status()

dog.walk()
bird.fly()

dog.show_status()
bird.show_status()

dog.show_toy()
bird.show_wing_span()