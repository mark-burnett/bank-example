class Ledger(object):
    def __init__(self, transactions):
        self.transactions = transactions

    def add_transaction(self, new_transaction):
        new_transaction.execute()
        self.transactions.append(new_transaction)

    def __str__(self):
        lines = [str(transaction) for transaction in self.transactions]
        return '\n'.join(lines)
