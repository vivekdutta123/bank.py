#filename = input("Enter the filename: ")
#fh = open(filename)

# Loop through each line in the file
##for line in fh:
    # Check if the line starts with "Hellow"
    #if line.startswith("Hellow"):
        #print(line.strip())  # .strip() removes leading/trailing whitespace

# Close the file after processing
#fh.close()
#filename = input("Enter the filename: ")
#fh = open(filename)
#count=0
#for line in fh:
    #count=count+1
#print("line count:",count )
#fh = open(filename)

#for line in fh:
    #line = line.rstrip()
    #if line.startswith("Hellow"):
        #print(line)

#fh.close()
#filename = input("Enter the filename: ")
#fh = open(filename)

#for line in fh:
    #line = line.rstrip()  # Remove trailing whitespace, including newline characters
    #if line.find("Hellow") != -1:  # Check if "Hellow" is present in the line
        #print(line)

#fh.close()
#filename = input("Enter a filename: ")
#fh = open(filename, "w")
#print(fh)
#fh.close()

with open('destination.txt', 'w') as fout:
    line1 = "This here's the wattle,\n"
    fout.write(line1)

