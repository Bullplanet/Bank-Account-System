# Mini Project - Bank Account System

import random


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(100000, 999999)
        self.balance = 0
        self.transaction_history = []


    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited, Current balance is: ${self.balance}")
            self.transaction_history.append(f"Deposited: ${amount}, Balance: ${self.balance}")
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
            self.transaction_history.append("Withdrawal failed:  invalid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. Current balance is: ${self.balance}")
            self.transaction_history.append(f"Withdrawn: ${amount}")
        else:
            print("Insufficient balance")
            self.transaction_history.append("Withdrawal failed:  Insufficient balance")

    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

    def display_info(self):
        print(f"Account holder name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: ${self.balance}")

    def transfer(self, amount, target_account):

        if amount <= 0:
            print("Transaction failed: Enter a valid amount")
            self.transaction_history.append("Transfer failed: Invalid amount")
        elif amount > self.balance:
            print("Transaction failed: Insufficient funds")
            self.transaction_history.append("Transaction failed: Insufficient funds")
        else:
            self.balance -= amount
            target_account.balance += amount
            print(f"${amount} transferred to {target_account.name}. Your current balance is: ${self.balance}")
            self.transaction_history.append(f"${amount} transferred to {target_account.name}, Balance: ${self.balance}")
            target_account.transaction_history.append(f"{amount} received from {self.name}")

    def show_transaction_history(self):
        print(f"Transaction history of {self.name}")
        for transaction in self.transaction_history:
            print("-", transaction)

    def apply_interest(self, rate):
        interest = round(self.balance * (rate / 100), 2)
        self.balance += interest
        print(f"Interest of ${interest} applied at {rate}% rate. New balance: ${self.balance}")
        self.transaction_history.append(f"Interest applied: ${interest}")


account1 = BankAccount("Oliver Queen")
account2 = BankAccount("Barry Allen")


while True:
    print("\n--- Welcome to KN Bank System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Transfer")
    print("5. Show Account Info")
    print("6. Show Transaction History")
    print("7. Apply Interest")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        account1.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        account1.withdraw(amount)

    elif choice == '3':
        account1.get_balance()

    elif choice == '4':
        amount = float(input("Enter the amount to transfer: "))
        target_account = input("Enter account holder name: ")

        if target_account == account2.name:
            account1.transfer(amount, account2)
        else:
            print("Target account not found!")

    elif choice == '5':
        account1.display_info()

    elif choice == '6':
        account1.show_transaction_history()

    elif choice == '7':
        rate = float(input("Enter the percentage of rate: "))
        account1.apply_interest(rate)

    elif choice == "8":
        print("Thank You!, Exiting")

    else:
        print("Invalid choice. Please select a number between 1 and 8.")





