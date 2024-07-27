filename = input("Enter the filename: ")
fh=open(filename)
for line in fh:
    fx=line.rstrip()
    print(fx.upper())
