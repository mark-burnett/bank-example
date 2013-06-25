from bank import factory
from bank import request
from bank.memory_storage import MemoryStorage


def send_request(dispatcher, request_name, **kwargs):
    rq = request.create_request(request_name, **kwargs)
    return dispatcher.dispatch(rq)


def make_set_of_accounts(dispatcher):
    response = send_request(dispatcher,
            'create_set_of_accounts', name='Example Accounts')
    return response.data['set_of_accounts'], response.data['ledger']


def make_account(soa, dispatcher, name, account_type):
    response = send_request(dispatcher, 'create_account',
            set_of_accounts=soa, name=name, account_type=account_type)
    return response.data


def make_accounts(soa, dispatcher, accounts):
    account_ids = {}
    for name, account_type in accounts:
        account_ids[name] = make_account(soa, dispatcher, name, account_type)

    return account_ids


def make_transaction(ledger, dispatcher, **kwargs):
    response = send_request(dispatcher, 'create_transaction',
            ledger=ledger, **kwargs)

    return response.data



def report(object_id, dispatcher):
    request_class = request.get_request_class('report')
    rq = request_class(object_id=object_id)
    response = dispatcher.dispatch(rq)

    return response.data


def main(dispatcher):
    account_list = [
        ('Checking Account', 'asset'),
        ('Salary', 'income'),
        ('Expenses', 'expense'),
    ]
    soa, ledger = make_set_of_accounts(dispatcher)
    accounts = make_accounts(soa, dispatcher, account_list)

    print 'Initial balances'
    print '----------------'
    print report(soa, dispatcher)

    make_transaction(ledger, dispatcher,
            description='Payday',
            debits=[(accounts['Salary'], 100)],
            credits=[(accounts['Checking Account'], 100)],
            timestamp='April 25, 1992')

    make_transaction(ledger, dispatcher,
            description='Gas mask',
            debits=[(accounts['Checking Account'], 72)],
            credits=[(accounts['Expenses'], 72)],
            timestamp='April 26, 1992')

    print
    print 'Transactions'
    print '------------'
    print report(ledger, dispatcher)

    print
    print 'Final balances'
    print '--------------'
    print report(soa, dispatcher)


if __name__ == '__main__':
    storage = MemoryStorage({})
    dispatcher = factory.make_dispatcher(storage)

    main(dispatcher)
