import unittest
from src.bank_account import BankAccount
import os

class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(balance=100, log_file="transactions.txt")

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def test_deposit(self):
        new_balance = self.account.deposit(23)
        self.assertEqual(new_balance, 123, "El balance no es el esperado")

    def test_withdraw(self):
        new_balance = self.account.withdraw(23)
        self.assertEqual(new_balance, 77, "El balance no es el esperado")

    def test_get_balance(self):
        new_balance = self.account.get_balance()
        self.assertEqual(new_balance, 100, "El balance no es el esperado")

    def test__log_transaction(self):
        self.account.deposit(23)
        self.assertTrue(os.path.exists(self.account.log_file), "El archivo de log no existe")

    def _count_lines(self, file_path):
        with open(file_path, "r") as f:
            return len(f.readlines())

    def test_count_transactions(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
