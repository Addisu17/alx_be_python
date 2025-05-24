
monthly_income = int(input('Enter your monthly income: '))
monthly_expense = int(input('Enter your total monthly expenses: '))

monthly_saving = int(monthly_income - monthly_expense)
projected_savings = int(monthly_saving * 12 + int(monthly_saving * 12 * 0.05))

print(f'Enter your monthly income: {monthly_income}')
print(f'Enter your total monthly expenses: {monthly_expense}')
print(f'Your monthly savings are ${monthly_saving}. ')
print(f'Projected savings after one year, with interest, is: ${projected_savings}.')

