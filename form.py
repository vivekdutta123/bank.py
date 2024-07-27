filename = input("Enter the filename: ")
with open(filename, 'r') as fh:
    for line in fh:
        fx = line.rstrip()
        if fx.startswith("from"):
            words = fx.split()
            for word in words[1:]:
                print(word)
