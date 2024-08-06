import getpass

class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction_type, amount, balance):
        self.transactions.append({
            "type": transaction_type,
            "amount": amount,
            "balance": balance
        })

    def display(self):
        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(f"{transaction['type']}: Amount ${transaction['amount']}, Balance ${transaction['balance']}")
        print("--- End of History ---\n")


class ATM:
    def __init__(self):
        self.balance = 1000
        self.pin = None
        self.transaction_history = TransactionHistory()

    def set_initial_pin(self):
        while True:
            new_pin = getpass.getpass("Set your new PIN: ")
            confirm_pin = getpass.getpass("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN setup successful.")
                break
            else:
                print("PINs do not match. Please try again.")

    def login(self):
        if self.pin is None:
            self.set_initial_pin()
        attempts = 3
        while attempts > 0:
            entered_pin = getpass.getpass("Enter your PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        return False

    def display_menu(self):
        print("\n--- ATM Menu ---")
        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")
        return input("Please choose an option: ")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.add_transaction("Balance Inquiry", 0, self.balance)

    def withdraw_cash(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is: ${self.balance}")
            self.transaction_history.add_transaction("Withdrawal", amount, self.balance)

    def deposit_cash(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Deposit successful. Your new balance is: ${self.balance}")
        self.transaction_history.add_transaction("Deposit", amount, self.balance)

    def change_pin(self):
        current_pin = getpass.getpass("Enter current PIN: ")
        if current_pin == self.pin:
            new_pin = getpass.getpass("Enter new PIN: ")
            self.pin = new_pin
            print("PIN change successful.")
        else:
            print("Incorrect current PIN.")

    def view_transaction_history(self):
        self.transaction_history.display()


def main():
    atm = ATM()
    while True:
        if atm.login():
            while True:
                choice = atm.display_menu()
                if choice == '1':
                    atm.check_balance()
                elif choice == '2':
                    atm.withdraw_cash()
                elif choice == '3':
                    atm.deposit_cash()
                elif choice == '4':
                    atm.change_pin()
                elif choice == '5':
                    atm.view_transaction_history()
                elif choice == '6':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid option, please try again.")
        else:
            print("Login failed. Please try again.")

if __name__ == "__main__":
    main()
