
def compute_pay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = 40 * 0.5 * rate
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay


hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

total_pay = compute_pay(hours, rate)

# Output the total pay
print("Total pay: $", total_pay)
