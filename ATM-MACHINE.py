class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def authenticate(self, input_pin):
        return self.pin == input_pin

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount:.2f} deposited successfully.")
            self.check_balance()
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
            self.check_balance()


def main():
    atm = ATM(pin="1234", balance=1000.00)

    print("===== Welcome to the ATM =====")
    input_pin = input("Enter your 4-digit PIN: ")

    if not atm.authenticate(input_pin):
        print("Invalid PIN. Exiting...")
        return

    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
