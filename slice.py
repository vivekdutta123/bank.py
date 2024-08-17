# Get the limit from the user
limit = int(input("Enter the number of elements: "))

n = []  # Initialize an empty list

# Collect elements from the user
for _ in range(limit):  # Loop runs 'limit' times
    element = int(input("Enter an element: "))
    n.append(element)  # Append the actual element to the list

# Display the list of elements
print("List of elements:", n)
#short list using bubble sort
a=len(n)
for i in range(n):
    for j in range(0,n-i-1):
      if n[j]> n[j+1]:
         n[j]+n[j+1] = n[j+1]+n[j]
print("after sorting of list".n)
