class BankError(object):
    pass


class DuplicateAccountError(BankError, RuntimeError):
    def __init__(self, bad_account, set_of_accounts):
        self.bad_account = bad_account
        self.set_of_accounts = set_of_accounts

    def __str__(self):
        return '\n'.join([
            '\nAttempted to add account:',
            str(self.bad_account),
            'to set of accounts:',
            str(self.set_of_accounts)
        ])


class InvalidTransactionError(BankError, ValueError):
    def __init__(self, bad_transaction):
        self.bad_transaction = bad_transaction

    def __str__(self):
        return str(self.bad_transaction)


class InvalidRequestError(BankError, ValueError):
    def __init__(self, request, specific_message):
        self.request = request
        self.specific_message = specific_message

    def __str__(self):
        return 'account class = %s\n%s' % (self.request.classpath,
                self.specific_message)


class UnknownRequestError(BankError, RuntimeError):
    def __init__(self, request_name):
        self.request_name = request_name

    def __str__(self):
        return 'Could not find request matching name "%s".' % self.request_name


class RequestFailure(BankError, RuntimeError):
    def __init__(self, request, response):
        self.request = request
        self.response = response

    def __str__(self):
        return '\n%s\n%s' % (self.request, self.response)
