fhand = open("destination.txt")
count = 0
for line in fhand:
    if line.startswith("Hellow:"):
        print(line)
fhand.close()  # Remember to close the file when done
