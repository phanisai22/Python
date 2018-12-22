import datetime
import pytz


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        print('The account is added for {} with a _balance {} rs'.format(name, balance))
        self._transaction = [(Account._current_time(), balance, 'deposited')]

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            print('Deposited {} rs to your account .'.format(amount))
            self.show_balance()
            self._transaction.append((Account._current_time(),
                                      amount, 'deposited'))

    def withdraw(self, amount):
        if (self._balance - amount) >= 0:
            self._balance -= amount
            print('Withdrawn {} rs . Balance account is {} rs .'
                  .format(amount, self._balance))
            self._transaction.append((Account._current_time(),
                                      amount, 'withdrawn'))
        else:
            print('Cannot remove the requested amount of {} rs. Not enough _balance .'
                  .format(amount))
            self.show_balance()

    def show_balance(self):
        print('Account : {} \nBalance : {}'.format(self._name, self._balance))

    def show_transaction(self):
        for date, amount, tran_type in self._transaction:
            # if amount > 0:
            #     tran_type = 'deposited'
            # else:
            #     tran_type = 'withdrawn'
            print("{:6} {} on {} (local time was {}) ."
                  .format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':

    phanisai = Account('phani sai', 1000)
    phanisai.deposit(500)
    # phanisai.show_balance()
    phanisai.withdraw(1600)
    phanisai.withdraw(1500)
    # phanisai.show_balance()
    phanisai.show_transaction()
