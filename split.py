filename = input("Enter the filename: ")
list = []

fh = open(filename)
for line in fh:
    fx = line.rstrip()
    words = fx.split()
    for word in list:
        if word not in list:
            list.append(word)
fh.close()

list.sort()
print("Unique words in alphabetical order:")
for word in list:
    print(word)
