annual_salary = int (input("Enter your annual salary: "))
monthly_salary = annual_salary/12
portion_saved = float (input("Enter the percent of salary to save, as a decimal: "))
monthly_savings = monthly_salary * portion_saved
total_cost = int(input("Enter the cost of your dream home: "))
partial_down_payment = 0.25 * total_cost

semi_annual_raise = float (input("Enter the semi annual raise, as a decimal: "))


number_of_months = 0
current_savings = 0

while current_savings < partial_down_payment:
	current_savings += (current_savings * 0.04/12) + monthly_savings
	number_of_months += 1

print("Number of Months: ", number_of_months)