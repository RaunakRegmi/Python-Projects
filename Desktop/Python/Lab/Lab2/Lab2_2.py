import math

a = int(input('Enter side a: '))
b = int(input('Enter  side b: '))
c = int(input('Enter side c: '))

if a <= (b + c) and b <= (a + c) and c <= (b + c):

    perimeter = a + b + c
    print(f'The perimeter is {perimeter}.')

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f'The area is {area}.')

else:
    print("The sides aren't valid")