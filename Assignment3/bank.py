from datetime import datetime

existing_accounts = set([])

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return (
            f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"{self.transaction_type}: {self.amount}\n"
        )


class PersonalAccount:
    def __init__(self, account_number, account_holder):
        if account_number not in existing_accounts:
            self.account_number = account_number
            self.account_holder = account_holder
            self.balance = 0.0
            self.transactions = []
        else:
            print('account with this id exists')

    def deposit(self, amount):
        if amount <= 0:
            print('error')

        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('error')

        if amount > self.balance:
            print('not enough money')

        transaction = Amount(amount, "WITHDRAWAL")
        self.transactions.append(transaction)
        self.balance -= amount

    def print_transaction_history(self):
        if not self.transactions:
            print("No transactions available.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def get_balance(self):
        print(self.balance)

    def get_account_number(self):
        print(self.account_number)

    def set_account_number(self, account_number):
        if account_number not in existing_accounts:
            self.account_number = account_number
        else:
            print('account with this id exists')

    def get_account_holder(self):
        print(self.account_holder)

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance: {self.balance:.2f}"
        )

    def __add__(self, amount):
        self.deposit(amount)
        return self.balance

    def __sub__(self, amount):
        self.withdraw(amount)
        return self.balance



account = PersonalAccount(1001, "Alice")

account.deposit(1000)
account.withdraw(300)

account.get_balance()
account.print_transaction_history()