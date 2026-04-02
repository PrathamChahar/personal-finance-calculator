print("===== Personal Finance Calculator =====")

name = input("Enter your name: ")
income = float(input("Enter your monthly income (₹): "))
rent = float(input("Enter your rent (₹): "))
food = float(input("Enter your food expenses (₹): "))
other = float(input("Enter other expenses (₹): "))

total_expenses = rent + food + other
savings = income - total_expenses
savings_percent = (savings / income) * 100

print("\n--- Your Financial Summary ---")
print("Name:", name)
print("Total Income: ₹", income)
print("Total Expenses: ₹", total_expenses)
print("Monthly Savings: ₹", savings)
print("Savings Percentage:", round(savings_percent, 2), "%")

if savings_percent >= 20:
    print("Great job! You are saving well.")
elif savings_percent >= 10:
    print("Decent savings. Try to cut some expenses.")
else:
    print("Warning: Your savings are too low!")