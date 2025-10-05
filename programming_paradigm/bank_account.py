class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self._account_balance = initial_balance  # private variable

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self._account_balance += amount
            return True
        return False  # failed deposit

    def withdraw(self, amount):
        """Withdraw money if enough balance is available."""
        if amount <= 0:
            return False  # invalid withdrawal
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        # Only print when insufficient funds
        print("Insufficient funds.")
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
