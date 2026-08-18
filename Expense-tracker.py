FILE_NAME = "expenses.txt"


def add_expense():
    name = input("Enter expense: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a") as file:
        file.write(name + "|" + str(amount) + "\n")

    print("Expense added!")


def view_expenses():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, amount = line.strip().split("|")
                print(name, "-", amount)
                total += float(amount)

            print("Total:", total)

    except FileNotFoundError:
        print("No expenses found.")


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        break

    else:
        print("Invalid choice!")