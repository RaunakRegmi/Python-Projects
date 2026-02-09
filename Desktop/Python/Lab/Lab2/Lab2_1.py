year = int(input('Enter the year: '))

if not year % 4 == 0:
    print(f'{year} is not a Leap Year because it is not divisible by 4')

elif not year % 100 == 0:
    print(f'{year} is Leap Year because it is not divisible by 100')

elif not year % 400 == 0:
    print(f'{year} is not a Leap Year because it is not divisible by 400')

else:
    print(f'{year} is a Leap Year, because it is divisible by 400')

