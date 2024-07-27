filename = input("Enter the filename: ")

fh = open(filename,'r')
for line in fh:
    fx = line.rstrip()
    if line startwith("from")
    word=line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
fh.close()

unique_words.sort()
print("Unique words in alphabetical order:")
for word in unique_words:
    print(word)
