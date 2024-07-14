# Input for hours worked and hourly rate
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Compute regular and overtime pay
if hours > 40:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * rate * 1.5
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours * rate

# Output the total pay
print("Total pay: $", total_pay)
