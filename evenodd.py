def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
num = int(input("Enter a number: "))
print("The number is .", check_odd_or_even(num))
