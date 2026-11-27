class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self, message):
        print(f"{self.recipient}に通知：{message}")

class EmailNotification(Notification):
    def send(self, message):
        print(f"メール({self.recipient}) :{message}")

class AppNotification(Notification):
    def send(self, message):
        print(f"アプリ通知 ({self.recipient}) :{message}")


notice = Notification("山田")
email = EmailNotification("田中")
app = AppNotification("佐藤")

notice.send("明日の授業は9時開始です")
email.send("明日の授業は9時開始です")
app.send("明日の授業は9時開始です")



