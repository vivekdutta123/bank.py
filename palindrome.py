# Input string
s = input("Enter a string: ")

# Normalize the string
s = s.replace(" ", "").lower()

# Check if the string is a palindrome
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
