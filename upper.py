# Define the file path
file_path = 'example.txt'  # Replace 'example.txt' with your file name

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read and print each line in uppercase
    for line in file:
        print(line.upper().strip())
