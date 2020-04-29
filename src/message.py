class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def get_sender(self):
        return self.sender

    def get_content(self):
        return self.content

    def __str__(self):
        return self.sender + ": " + self.content

    def __eq__(self,other):
        if isinstance(other, Message):
            return (self.sender == other.sender and self.content == other.content)
        return False
