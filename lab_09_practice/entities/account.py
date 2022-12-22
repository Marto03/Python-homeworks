class Account:
    def __init__(self, balance, currency, acc_type, IBAN="BG9812"):
        self.balance = balance
        self.currency = currency
        self.acc_type = acc_type
        self.IBAN = IBAN

    def print(self):
        print(f"{self.balance, self.currency, self.acc_type, self.IBAN}")
