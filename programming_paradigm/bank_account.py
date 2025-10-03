# Bank Account Class
# This module contains the BankAccount class for basic banking operations

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount from account balance if sufficient funds exist.
        
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
      
