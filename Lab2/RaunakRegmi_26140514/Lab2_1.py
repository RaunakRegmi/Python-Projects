hourly_wage = 22
standard_hours = 40
overtime_rate = 1.5

employee_name = str(input("Enter employee's Name: "))

hours_worked = float(input("Enter hours worked: "))

print(f'Employee Name {employee_name}')

if hours_worked <= 40:
    regular_pay = hours_worked * hourly_wage
    print(f'Regular Pay: {regular_pay}')

    overtime_pay = 0
    print(f'Overtime Pay: {overtime_pay}')

    total = regular_pay + overtime_pay
    print(f'Total Pay: {total}')

elif hours_worked > 40:
    regular_hours = 40
    regular_pay = regular_hours * hourly_wage
    print(f'Regular Pay: {regular_pay}')

    overtime_hours = hours_worked - regular_hours
    overtime_pay = overtime_hours * (22 * overtime_rate)
    print(f'Overtime Pay: {overtime_pay}')

    total = regular_pay + overtime_pay
    print(f'Total Pay: {total}')

else:
    pass