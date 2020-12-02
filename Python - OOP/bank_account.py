class Account:

    _balance = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def deposit(self, password, money):
        if password == self.password:
            self._balance += money

    def view_money(self, password):
        if password == self.password:
            return self._balance

my_account = Account("Hitu", "email", "1234")

my_account.deposit("1234", 1000000)

print(my_account._balance)
print(my_account.view_money("1234"))

