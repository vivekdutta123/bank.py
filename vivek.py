#max and min of three numbers using function
def find_maximum(a, b, c):
    if a >= b and a >= c:
        print("a is maximum")
    elif b >= a and b >= c:
        print("b is maximum")
    elif c >= a and c >= b:
        print("c is maximum")
    else:
        print("All numbers are equal")

# Example usage
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

find_maximum(a, b, c)
