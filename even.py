def even_numbers(a,b):
    for number in range(a,b+1):
        if number % 2 == 0:
            print(number)
even_numbers(1, 10)

#sorted string
sample_string = input("Enter a space-separated sequence of words: ")

# Split the input string into words
words = sample_string.split("-")

# Sort the list of words
sorted_words = sorted(words)

# Join the sorted list of words into a single string with spaces
sorted_string = "- ".join(sorted_words)

# Print the sorted string
print(sorted_string)
