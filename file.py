filename = input("Enter the filename: ")
fh = open(filename)

# Loop through each line in the file
for line in fh:
    # Check if the line contains "Hellow"
    if "Hellow" in line:
        print(line.strip())  # .strip() removes leading/trailing whitespace

# Close the file after processing
fh.close()
