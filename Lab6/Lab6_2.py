def main():
    contacts = []
    contacts.append(("Miles", "001"))
    contacts.append(("Jones", "002"))

    while True:
        print()
        print("Select an operation:")
        print("v view contacts")
        print("a add contact")
        print("d delete contact")
        print("q quit")
        print()

        choice = input("Enter choice (v/a/d/q): ")
        choice = choice.lower()

        if choice != "v" and choice != "a" and choice != "d" and choice != "q":
            print()
            print("------- Invalid choice -------")
            print("Try again...")
            continue

        if choice == "v":
            view_contacts(contacts)


        elif choice == "a":
            add_contact(contacts)

        elif choice == "d":
            delete_contact(contacts)


        elif choice == "q":
            print("Exiting program...")
            break


def view_contacts(contact):
    print()
    print("------- view_contacts -------")
    print()

    if len(contact) == 0:
        print("No contacts to display!")
        return

    count = 1

    for item in contact:
        name = item[0]
        number = item[1]
        print(count, name, "        ", number)
        count = count + 1


def add_contact(contact):
    print()
    print("------- add_contact -------")
    print()

    name = input("Enter contact name: ")
    number = input("Enter contact number: ")

    new_contact = (name, number)

    # adding to list
    contact.append(new_contact)

    print(name, "-", number, "has been added into the contact list")


def delete_contact(contact):
    print()
    print("------- delete_contact -------")
    print()

    if len(contact) == 0:
        print("No contacts to delete!")
        return

    index = 1
    for item in contact:
        print(index, item[0], "        ", item[1])
        index = index + 1

    user_input = input("Enter the ID of the contact to delete: ")

    if user_input.isdigit() == False:
        print("Please enter a valid number!")
        return

    id = int(user_input)

    if id < 1 or id > len(contact):
        print("Invalid ID!")
        return

    deleted_contact = contact[id - 1]
    contact.remove(deleted_contact)

    print("Deleting:", deleted_contact[0])


if __name__ == "__main__":
    main()
