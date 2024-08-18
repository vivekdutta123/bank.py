fhand = open("Rj.txt")
count = 0
for line in fhand:
    if line.startswith("the:"):
        print(line)
fhand.close()  # Remember to close the file when done
