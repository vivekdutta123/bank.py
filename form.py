filename = input("Enter the filename: ")
fh = open(filename,'r')
for line in fh:
    fx = line.rstrip()
    if fx startwith("from"):
     words=fx.split()
     for word in words[1:]:
      print(word)
