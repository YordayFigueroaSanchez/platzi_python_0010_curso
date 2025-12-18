import unittest
from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit(self):
        new_balance = self.account.deposit(23)
        assert new_balance == 123

    def test_withdraw(self):
        new_balance = self.account.withdraw(23)
        assert new_balance == 77

    def test_get_balance(self):
        new_balance = self.account.get_balance()
        assert new_balance == 100
