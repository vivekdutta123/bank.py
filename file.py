fhand = open("Rj.txt")
count=0
for line in fhand:
    if line.startwith("the:"):
       print(line)
