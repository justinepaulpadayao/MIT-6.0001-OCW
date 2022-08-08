annual_salary = float(input('Enter the starting salary: '))
semi_annual_raise = 0.07
annual_return = 0.04
total_cost = 1000000
down_payment = 0.25(total_cost)

# Core Variables
portion_down_payment = 0.25*(total_cost)
current_savings = 0
r = 0.04
month = 0
monthly_salary = annual_salary/12
portion_saved = 0
low = 0
high = 1


while current_savings <= portion_down_payment:
    while month <= 36:
        if month != 0 and month % 6 == 0:
            monthly_salary = monthly_salary + monthly_salary*semi_annual_raise
        savings_return = current_savings*r/12
        current_savings = current_savings + savings_return + portion_saved*monthly_salary
        portion_saved = (low + high)/2
        month += 1

print('Number of months: ', month)


