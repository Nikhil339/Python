class Bank:
    def Account(self, name, initial_balance = 0):
        self.name = name
        self.balance = initial_balance
        print(f"Congratulations, you have successfully created an account:\nName:{self.name}\nBalance: ₹{self.balance}")
    
    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Amount must be positive.")

    def Withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        elif amount > self.balance:
            print("Insufficient account balance.")
        else:
            print("Amount must be positive.")

    def CheckBalance(self):
        print(f"Account name: {self.name}")
        print(f"Account balance: ₹{self.balance}")

def main():
    accounts = {}

    while True:
        print()
        print("Welcome to XYZ Bank")
        print("Select from the following options: ")
        print("1. Create account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")
        print()
        option = int(input("Option number: "))

        if option == 1:
            print()
            name = input("Enter account name: ")
            if name in accounts:
                print("Account already exists.")
            else:
                accounts[name] = Bank()
                accounts[name].Account(name)
        elif option == 2:
            print()
            name = input("Enter account name: ")
            if name in accounts:
                amount = float(input("Enter amount to deposit: ₹"))
                accounts[name].Deposit(amount)
            else:
                print("Account not found.")
        elif option == 3:
            print()
            name = input("Enter account name: ")
            if name in accounts:
                amount = float(input("Enter amount to withdraw: ₹"))
                accounts[name].Withdraw(amount)
            else:
                print("Account not found.")
        elif option == 4:
            print()
            if name in accounts:
                name= input("Enter account name: ")
                accounts[name].CheckBalance()
            else:
                print("Account not found.")
        elif option == 5:
            print()
            print("Thank you!")
            break
        else:
            print("Invalid! Select from the given options.")

main()