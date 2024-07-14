def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
num = int(input("Enter a number: "))
result = check_odd_or_even(num)
print("The number is .", result)
