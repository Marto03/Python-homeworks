class User:
    def __init__(self, account, names, EGN):
        self.account = account
        self.names = names
        self.EGN = EGN

    def print(self):
        print(f"{self.account, self.names, self.EGN}")
