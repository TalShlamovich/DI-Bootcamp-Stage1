# Creating class

from mimetypes import init
from typing_extensions import Self


class BankAccount():

    def __init__(self, holder: str, number: int, balance: int) -> Self:
        self._holder =  holder #_ protected
        self.__number = number #__private
        self._balance = balance


    # def deposit(self, amount: int):
    #     if amount > 0:
    #         self._balance += amount

    @property
    def holder(self):
        return self._holder

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self._balance += amount

        
# create class with inheritance

class StudentAccount(BankAccount):
    def __init__(self, holder: str, number: int, balance: int, student_id: str) -> Self:
        super().__init__(holder, number, balance)
        self.student_id = student_id



student = StudentAccount('Brad', 782645, 654, 'A87365H54')
print(student.__dict__) #shows both private and protected

student.balance+=1000
print(student.balance)
