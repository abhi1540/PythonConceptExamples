import datetime
import pytz


class Account(object):
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    # _ before method name means it is non public.
    # when we have a function and inside function if we are not using self then make that function as static.
    # static function can be accessible from both class and its instance

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self.__name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self.__transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self.__transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()

    tim.withdraw(2000)

    tim.show_transactions()
    new_acc = Account("Abhi", 700)
    new_acc.__balance = 200  #
    new_acc.deposit(200)
    new_acc.withdraw(300)
    new_acc.show_transactions()