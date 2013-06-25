from bank import exceptions


class SetOfAccounts(object):
    def __init__(self, name, accounts, ledger):
        self.name = name
        self.accounts = accounts
        self.ledger = ledger

    def add_account(self, new_account):
        if new_account.name in self.accounts:
            raise exceptions.DuplicateAccountError(new_account, self)
        else:
            self.accounts[new_account.name] = new_account

    def __str__(self):
        lines = [self.name]
        lines += [str(account) for account in self.accounts.itervalues()]
        return '\n'.join(lines)
