def add_guest(list1):
    name = input("Enter guest name: ")
    list1.append(name)
    print(name, "is added.")


def remove_guest(list1):
    name = input("Enter the name of guest which you want to remove:")

    if name in list1:
        list1.remove(name)
        print(name, "is removed.")
    else:
        print("Guest not found.")


def print_guests(list1):
    sorted_list = sorted(list1)

    print("Guest list:")
    for i in sorted_list:
        print(i)


def main():

    guests = []

    while True:

        print()
        print("A Add guest")
        print("R Remove guest")
        print("P Print guest list")
        print("Q Quit")

        ch = input("Enter choice: ")

        if ch == "A":
            add_guest(guests)

        elif ch == "R":
            remove_guest(guests)

        elif ch == "P":
            print_guests(guests)

        elif ch == "Q":
            print("Total guests:", len(guests))
            print("Goodbye! See you in the party!")
            break

        else:
            print("Invalid choice. Please choose a valid option (A, R, P or Q)")


main()



