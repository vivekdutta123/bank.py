filename = input("Enter the filename: ")
unique_words = []

try:
    fh = open(filename)
    for line in fh:
        fx = line.rstrip()
        words = fx.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    fh.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
else:
    unique_words.sort()
    print("Unique words in alphabetical order:")
    for word in unique_words:
        print(word)
