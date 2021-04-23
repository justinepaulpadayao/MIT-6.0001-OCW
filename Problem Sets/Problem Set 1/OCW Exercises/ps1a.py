
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# Core Variables
portion_down_payment = 0.25*(total_cost)
current_savings = 0
r = 0.04
month = 0
monthly_savings = portion_saved*(annual_salary/12)


while current_savings <= portion_down_payment:
    savings_return = current_savings*r/12
    current_savings = current_savings + savings_return + monthly_savings
    month = month + 1

print('Number of months: ', month)


