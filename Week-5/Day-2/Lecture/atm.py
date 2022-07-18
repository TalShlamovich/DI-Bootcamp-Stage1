class AtmAccount:

    available_account = 9991

    def __init__(self, holder) -> None:
        self.__holder = holder #__ private
        self._balance = 0.0 #_ protected
        
        self.__account_number = AtmAccount.available_account
        available_account +=1

    @property
    def show_balace(self):
        return self._balance

    @balance.setter
    def _balance(self, amount):
        self._balance += amount

    def deposit(self, amount):
        self._balance +=amount

    


account1 = AtmAccount('Yossi Eik')

# print(account1.account_number)