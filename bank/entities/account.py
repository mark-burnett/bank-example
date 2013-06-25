import abc


class BaseAccount(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @abc.abstractmethod
    def credit(self, amount):
        pass

    @abc.abstractmethod
    def debit(self, amount):
        pass

    def __str__(self):
        return '%20s: %10d' % (self.name, self.balance)


class CreditAccountBase(BaseAccount):
    def credit(self, amount):
        self.balance -= amount

    def debit(self, amount):
        self.balance += amount


class DebitAccountBase(BaseAccount):
    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        self.balance -= amount


class AssetAccount(DebitAccountBase):
    pass

class ExpenseAccount(DebitAccountBase):
    pass


class LiabilityAccount(CreditAccountBase):
    pass

class IncomeAccount(CreditAccountBase):
    pass

class EquityAccount(CreditAccountBase):
    pass
