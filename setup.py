from setuptools import setup, find_packages


entry_points = '''
[bank_handler_modules]
balance = bank.queries.balance
create_account = bank.commands.create_account
create_set_of_accounts = bank.commands.create_set_of_accounts
create_transaction = bank.commands.create_transaction
report = bank.queries.report
'''


setup(
        name='bank',
        version = '0.1',
        packages = find_packages(exclude=[
            'integration_tests',
            'unit_tests',
        ]),
        install_requires = [
            'python-dateutil',
        ],
        setup_requires = [
            'nose',
        ],
        tests_require = [
            'mock',
            'nose',
            'coverage',
        ],
        test_suite = 'unit_tests',
        entry_points=entry_points,
)
