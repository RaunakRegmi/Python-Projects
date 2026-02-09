class BankAccount:

    def __init__(self):
        self.balance = []
        self.balance.append(0.0)
        self.balance.append(0.0)
        self.acc_number = []
        self.acc_number.append("11")
        self.acc_number.append("22")

    def get_account(self):
        return self.acc_number

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance[0] = self.balance[0] + amount[0]

        self.balance[1] = self.balance[1] + amount[1]

        return self.balance

    def withdraw(self, amount):
        self.balance[0] = self.balance[0] - amount[0]

        self.balance[1] = self.balance[1] - amount[1]

        return self.balance

    def transfer(self, amount, acc):
        if acc == "11":
            self.balance[0] = self.balance[0] + amount
            self.balance[1] = self.balance[1] - amount

        elif acc == "22":
            self.balance[0] = self.balance[0] - amount
            self.balance[1] = self.balance[1] + amount


def main():
    bank = BankAccount()

    bank.deposit([100.0, 100.0])
    print(bank.get_balance())

    bank.deposit([20.0, 20.0])
    print(bank.get_balance())

    bank.transfer(20.0, "11")
    print(bank.get_balance())


main()
