starting_balance = 1000

customer_name = input("Enter your name: ")
print(f"Welcome {customer_name}")

while True:
    print("1. Make a Deposit")
    print("2. Make a Withdrawal")
    print("3. Obtain a Balance")
    print("4. Quit")

    user_choice = input("Select an option: ")

    if user_choice == '1':
        deposit_amount = float(input("Enter deposit amount: "))
        starting_balance = starting_balance + deposit_amount
        print(f"Deposited £{deposit_amount}")

    elif user_choice == '2':
        withdrawal_amount = float(input("Enter withdrawal amount: "))

        if withdrawal_amount > starting_balance:
            print("It is not possible to withdraw beyond the account balance")
        else:
            starting_balance = starting_balance - withdrawal_amount
            print(f"Withdrew £{withdrawal_amount}")

    elif user_choice == '3':
        print(f"Current balance: £{starting_balance}")

    elif user_choice == '4' or user_choice.upper() == 'Q':
        print("Thank you for using our service")
        break

    else:
        print("Invalid option. Please try again")
