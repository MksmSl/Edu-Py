
class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    # @classmethod
    # def create_account(cls, account_number):
    #     return cls(0.0, account_number)

    # def deposit(self, amount):
    #     if amount > 0:
    #         self._balance += amount
    #     else:
    #         raise ValueError('Amount must be positive')

    # def withdraw(self, amount):
    #     if amount > 0:
    #         self._balance -= amount
    #     else:
    #         raise ValueError('Amount must be positive')

    # def get_balance(self):
    #     return self._balance
    
    # def get_account_number(self):
    #     return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self._interest = interest

    def add_intersts(self):
        self._balance += self._balance*self._interest/100


    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}, interest: {self._interest}'    


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit


class Bank():
    def __init__(self, accounts: list[Account]):
        self.accounts = accounts


    def update(self):
        for i, val_acc in enumerate(self.accounts):
            if type(val_acc) == SavingsAccount:
                val_acc.add_intersts()
                print(val_acc)
            if type(val_acc) == CurrentAccount and val_acc._overdraft_limit < 0:
                print('send the letter')



my_save_acc = SavingsAccount(10000, 123456, 5)
my_curr_acc = CurrentAccount(-1000, 12345622, -1500)

mono = Bank([my_save_acc, my_curr_acc])

print(my_save_acc._balance)

mono.update()





class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'