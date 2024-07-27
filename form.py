# Open the file
filename = 'yourfile.txt'  # Replace with your file name

try:
    with open(filename, 'r') as file:
        for line in file:
            # Check if the line starts with "From"
            if line.startswith('From'):
                # Split the line into words
                words = line.split()
                # Print each line from the second word onward
                if len(words) > 1:
                    print(' '.join(words[1:]))
except FileNotFoundError:
    print(f"File {filename} not found.")

