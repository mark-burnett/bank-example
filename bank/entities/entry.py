import abc


class EntryBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, account, amount):
        self.account = account
        self.amount = int(amount)

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractproperty
    def credit_amount(self):
        pass

    @abc.abstractproperty
    def debit_amount(self):
        pass

    def __str__(self):
        return '%20s: %10d | %10d' % (self.account.name,
                self.debit_amount, self.credit_amount)

    def __eq__(self, other):
        return self.account == other.account and self.amount == other.amount


class CreditEntry(EntryBase):
    def execute(self):
        return self.account.credit(self.amount)

    @property
    def credit_amount(self):
        return self.amount

    @property
    def debit_amount(self):
        return 0


class DebitEntry(EntryBase):
    def execute(self):
        return self.account.debit(self.amount)

    @property
    def credit_amount(self):
        return 0

    @property
    def debit_amount(self):
        return self.amount
