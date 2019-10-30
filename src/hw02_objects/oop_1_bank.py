"""
Exercise 1: (5 points)

a) Using the slides & the script, put together a file
    containing the complete Account class.
    Each method must have a documentation string at the
    beginning which describes what the method is doing.
    (1 point)

b) Create a main application where you create a number of accounts.
    Play around with depositing / withdrawing money.
    Change the account holder of an account using a setter method.
    (1 point)

c) Change the withdraw function such that the minimum balance
    allowed is -1000.
    (1 point)

d) Write a function apply_interest(self) which applies an interest
    rate of 1.5% to the current balance and call it on your objects.
    (1 point)

e) Draw a UML diagram representing your Account class. (1 point)
"""


class Account:
    """ Here has to be a documentation string that describes
    which data objects this class is designed for.
    You have to remove the pass statement and then write some
    code for the class. """

    # CONSTRUCTOR DER KLASSE ACCOUNT
    def __init__(self, num, person):
        self.balance = 0
        self.number = num
        self.holder = person
    # METHODS

    """ * dies Method beschreibt die Auszahlung von Account.
    """
    def withdraw(self, amount):
        if((self.balance - amount ) <= 1000):
            self.balance -= amount
        else:
            print("Die Auszahlung ist nicht moeglich!")


    """ * dies Method beschreibt die Einzahlung von Account.
    """
    def deposit(self, amount):
        self.balance += amount
    """ * dies Set-Method beschreibt die Aenderung von Holder des Accountes. 
    """
    def setHolder(self,value):
        self.holder = value;
    def apply_interest(self):
        self.balance = self.belance + self.balance*(0, 0o15)

    """ * dies Method beschreibt die Informationen von Account.
    """
    def __str__(self):

        res = "*** Account Info ***\n"
        res += "Account ID:" + str(self.number) + "\n"
        res += "Holder:" + self.holder + "\n"
        res += "Balance: " + str(self.balance) + "\n"
        return res



if __name__ == "__main__":
    print("Welcome to the Python Bank!")
