filename = input("Enter the filename: ")
fh = open(filename)
# Loop through each line in the file
for line in fh:
    # Check if the line starts with "Hellow:"
    if line.startswith("Hellow:"):
        print(line)

# Close the file after processing
fh.close()
