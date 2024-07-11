# Get user input
sample_items = input("Enter a hyphen-separated sequence of words: ")

# Split the input sequence into words
words = sample_items.split('-')

# Sort the list of words
sorted_words = sorted(words)

# Join the sorted list of words into a single string with hyphens
sorted_sequence = '-'.join(sorted_words)

# Print the sorted sequence
print(sorted_sequence)

