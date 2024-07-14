total = 0
count = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input.lower() == 'done':
        break

    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a number or 'done' to finish.")

if count > 0:
    average = total / count
else:
    average = 0

print("Total",Total)
print("count",count)
print("Average", Average)
