class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction(f"Cuenta creada.")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(message + "\n")
        
    def deposit(self, amount):
        self.balance += amount
        self._log_transaction(f"Deposited {amount}, new balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        self._log_transaction(f"Withdrawn {amount}, new balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked balance: {self.balance}")
        return self.balance