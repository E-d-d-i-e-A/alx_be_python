# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with 5% interest
# Formula: (Monthly Saving * 12) + (Monthly Savings * 12 * 0.05)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output Results
print (f"Your monthly savings are ${monthly_savings}.")
print (f"Projected savings after one year, with interest, is: ${projected_savings}.")
