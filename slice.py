# Take the limit from the user
limit = int(input("Enter limit: "))

lst = []

# Collect elements from the user
for _ in range(limit):
    element = int(input("Enter element: "))
    lst.append(element)

print("Original list:", lst)

# Bubble sort algorithm
n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("After sorting, the list is:", lst)
