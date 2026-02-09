import math

number_to_check = int(input("Enter a number: "))

prime_flag = True
found_divisors = []

limit = int(math.sqrt(number_to_check)) + 1

for i in range(2, limit):

    if number_to_check % i == 0:
        prime_flag = False

        found_divisors.append(i)

if prime_flag == True:

    print(f"{number_to_check} is prime")
else:

    print(f"{number_to_check} is not prime")
    print(f"Divisors: {found_divisors}")
