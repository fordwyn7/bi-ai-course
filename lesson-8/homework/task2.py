import json


class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
        }

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])


class Bank:
    def __init__(self):
        self.accounts = {}
        self.file_path = "accounts.txt"
        self.load_from_file()
        self.next_account_number = self.get_next_account_number()

    def get_next_account_number(self):
        if not self.accounts:
            return 1001
        return max(int(acc) for acc in self.accounts) + 1

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        acc_num = str(self.next_account_number)
        new_account = Account(acc_num, name, initial_deposit)
        self.accounts[acc_num] = new_account
        self.next_account_number += 1
        self.save_to_file()
        return acc_num

    def view_account(self, account_number):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            return acc.to_dict()
        else:
            raise KeyError("Account not found.")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise KeyError("Account not found.")
        self.accounts[account_number].deposit(amount)
        self.save_to_file()

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise KeyError("Account not found.")
        self.accounts[account_number].withdraw(amount)
        self.save_to_file()

    def save_to_file(self):
        data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        with open(self.file_path, "r") as f:
            data = json.load(f)
            for acc_num, acc_data in data.items():
                self.accounts[acc_num] = Account.from_dict(acc_data)


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter your name: ")
                initial_deposit = float(input("Enter initial deposit amount: "))
                acc_num = bank.create_account(name, initial_deposit)
                print(
                    f"Account created successfully! Your account number is: {acc_num}"
                )

            elif choice == "2":
                acc_num = input("Enter your account number: ")
                details = bank.view_account(acc_num)
                print("\n--- Account Details ---")
                print(f"Account Number: {details['account_number']}")
                print(f"Name: {details['name']}")
                print(f"Balance: ${details['balance']:.2f}")

            elif choice == "3":
                acc_num = input("Enter your account number: ")
                amount = float(input("Enter deposit amount: "))
                bank.deposit(acc_num, amount)
                print("Deposit successful.")

            elif choice == "4":
                acc_num = input("Enter your account number: ")
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(acc_num, amount)
                print("Withdrawal successful.")

            elif choice == "5":
                print("Thank you for using the bank system.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyError as ke:
            print(f"Error: {ke}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
