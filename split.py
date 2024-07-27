# Prompt the user for the filename
filename = input("Enter the filename: ")

# Initialize an empty list to store unique words
unique_words = []

# Open the file
with open(filename, 'r') as file:
    # Read each line in the file
    for line in file:
        # Remove any trailing whitespace and split the line into words
        words = line.rstrip().split()

        # Check each word
        for word in words:
            # Convert the word to lowercase to ensure case-insensitive comparison
            word = word.lower()

            # Add the word to the list if it's not already present
            if word not in unique_words:
                unique_words.append(word)

# Sort the unique words in alphabetical order
unique_words.sort()

# Print the sorted unique words
print("Unique words in alphabetical order:")
for word in unique_words:
    print(word)
