from bank import exceptions


class Transaction(object):
    def __init__(self, timestamp, entries, description=''):
        self.timestamp = timestamp
        self.entries = entries
        self.description = description

    @property
    def credit_amount(self):
        return sum(entry.credit_amount for entry in self.entries)

    @property
    def debit_amount(self):
        return sum(entry.debit_amount for entry in self.entries)

    def execute(self):
        if self.is_valid():
            for entry in self.entries:
                entry.execute()

        else:
            raise exceptions.InvalidTransactionError(self)

    def is_valid(self):
        return self.credit_amount == self.debit_amount

    def __str__(self):
        lines = ['%s: %s' % (str(self.timestamp), self.description)]
        lines += map(str, self.entries)

        return '\n'.join(lines)
