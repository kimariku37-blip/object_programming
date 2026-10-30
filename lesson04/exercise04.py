class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return False
        
        self.is_borrowed = True
        return True

    def show_status(self):
        if self.is_borrowed:
            print(f"{self.title}：貸出中")
        else:
            print(f"{self.title}：貸出可能")


class Member:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        if book.borrow():
            print(f"{self.name}は「{book.title}」を借りました。")
        else:
            print(f"「{book.title}」は貸出中のため借りられません。")


book = Book("Python入門")

member1 = Member("田中")
member2 = Member("佐藤")

book.show_status()
print()

member1.borrow_book(book)
print()

book.show_status()
print()

member2.borrow_book(book)
print()

book.show_status()    