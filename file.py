# Open the file "destination.txt"
filename = input("Enter the filename: ")
fh=open(filename)
count = 0

# Loop through each line in the file
for line in fhand:
    # Check if the line starts with "Hellow:"
    if line.startswith("Hellow:"):
        print(line)

# Close the file after processing
fhand.close()
