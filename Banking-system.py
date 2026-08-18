FILE_NAME = "bank.txt"


def create_account():
    account_id = input("Enter account ID: ")
    name = input("Enter your name: ")
    balance = float(input("Enter initial balance: "))

    with open(FILE_NAME, "a") as file:
        file.write(account_id + "|" + name + "|" + str(balance) + "|0|No\n")

    print("Account created successfully!")


def find_account(account_id):
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if data[0] == account_id:
                    return data

    except FileNotFoundError:
        return None

    return None


def deposit():
    account_id = input("Enter account ID: ")
    account = find_account(account_id)

    if account is None:
        print("Account not found.")
        return

    amount = float(input("Enter deposit amount: "))

    account[2] = str(float(account[2]) + amount)

    update_account(account)

    print("Amount deposited successfully!")


def check_balance():
    account_id = input("Enter account ID: ")
    account = find_account(account_id)

    if account is None:
        print("Account not found.")
        return

    print("\nAccount ID:", account[0])
    print("Name:", account[1])
    print("Balance:", account[2])
    print("Loan:", account[3])
    print("Loan Status:", account[4])


def apply_loan():
    account_id = input("Enter account ID: ")
    account = find_account(account_id)

    if account is None:
        print("Account not found.")
        return

    balance = float(account[2])

    if balance > 50000:
        if account[4] == "Yes":
            print("You already have an approved loan.")
            return

        loan_amount = float(input("Enter loan amount: "))

        account[3] = str(loan_amount)
        account[4] = "Yes"

        update_account(account)

        print("Loan approved!")
        print("Loan amount:", loan_amount)

    else:
        print("You are not eligible for a loan.")
        print("Your balance must be more than 50000.")


def update_account(updated_account):
    accounts = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                account = line.strip().split("|")

                if account[0] == updated_account[0]:
                    accounts.append(updated_account)
                else:
                    accounts.append(account)

    except FileNotFoundError:
        return

    with open(FILE_NAME, "w") as file:
        for account in accounts:
            file.write("|".join(account) + "\n")


while True:
    print("\nBANKING SYSTEM")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Check Balance")
    print("4. Apply for Loan")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            check_balance()

        elif choice == "4":
            apply_loan()

        elif choice == "5":
            print("Thank you for using the Banking System!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")