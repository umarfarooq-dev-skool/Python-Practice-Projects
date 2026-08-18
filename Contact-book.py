FILE_NAME = "contacts.txt"


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "|" + phone + "\n")

    print("Contact saved!")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split("|")
                print(name, "-", phone)

    except FileNotFoundError:
        print("No contacts found.")


def search_contact():
    search = input("Enter name to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split("|")

                if name.lower() == search.lower():
                    print("Name:", name)
                    print("Phone:", phone)
                    return

        print("Contact not found.")

    except FileNotFoundError:
        print("No contacts found.")


while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        break

    else:
        print("Invalid choice!")