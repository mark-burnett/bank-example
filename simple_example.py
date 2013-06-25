from bank.entities import account
from bank.entities import entry
from bank.entities import ledger
from bank.entities import set_of_accounts
from bank.entities import transaction

from dateutil.parser import parse as parse_date


def main():
    general_ledger = ledger.Ledger([])

    soa = set_of_accounts.SetOfAccounts(name='Example Accounts',
            accounts={}, ledger=general_ledger)

    checkng_account = account.AssetAccount(name='Checking Account', balance=0)
    salary_account  = account.IncomeAccount(name='Salary', balance=0)
    expense_account = account.ExpenseAccount(name='Expenses', balance=0)

    soa.add_account(checkng_account)
    soa.add_account(salary_account)
    soa.add_account(expense_account)


    print 'Initial balances'
    print '----------------'
    print soa


    # Perform some transactions
    general_ledger.add_transaction(transaction.Transaction(
        timestamp=parse_date('April 25, 1992'),
        description='Payday',
        entries=[
            entry.CreditEntry(account=checkng_account, amount=100),
            entry.DebitEntry(account=salary_account, amount=100),
    ]))


    general_ledger.add_transaction(transaction.Transaction(
        timestamp=parse_date('April 26, 1992'),
        description='Gas mask',
        entries=[
            entry.CreditEntry(account=expense_account, amount=72),
            entry.DebitEntry(account=checkng_account, amount=72),
    ]))


    print
    print 'Transactions'
    print '------------'
    print general_ledger

    print
    print 'Final balances'
    print '--------------'
    print soa


if __name__ == '__main__':
    main()
