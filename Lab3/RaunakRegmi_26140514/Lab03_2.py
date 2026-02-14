attempts = 0

while attempts < 5:

    password = input("Enter the password: ")

    if password == "test100":
        print("You are logged in.")
        break

    attempts = attempts + 1

if attempts == 5:

    print("You've reached the maximum log in attempts.")