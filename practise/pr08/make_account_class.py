from make_class import make_class


def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""
    interest = 0.02

    def __init__(self, account_holder):
        self["set"]("holder", account_holder)
        self["set"]("balance", 0)

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        new_balance = self["get"]("balance") + amount
        self["set"]("balance", new_balance)
        return self["get"]("balance")

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self["get"]("balance")
        if amount > balance:
            return "Insufficient funds"
        self["set"]("balance", balance - amount)
        return self["get"]("balance")

    return make_class(locals())


def make_checking_account_class():
    """Return the CheckingAccount class, which imposes a $1 withdrawal fee."""
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        fee = self["get"]("withdraw_fee")
        return Account["get"]["withdraw"](self, amount + fee)

    return make_class(locals(), Account)


Account = make_account_class()
kirk_account = Account["new"]("Kirk")
print(kirk_account["get"]("holder"))
print(kirk_account["get"]("interest"))
kirk_account["get"]("deposit")(20)
kirk_account["get"]("withdraw")(5)
print(kirk_account["get"]("balance"))
kirk_account["set"]("interest", 0.04)
print(Account["get"]("interest"))

CheckingAccount = make_checking_account_class()
jack_acct = CheckingAccount["new"]("Jack")
print(jack_acct["get"]("interest"))
