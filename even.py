def even_numbers(a,b):
    for number in range(a,b+1):
        if number % 2 == 0:
            print(number)
even_numbers(1, 10)

#sorted string
def sort_hyphen(string_list):
    print("enter a string:-")
    words = string_list.split("-")  # Split the string by hyphen
    sorted_words = sorted(words)    # Sort the list of words
    sorted_string = "-".join(sorted_words)  # Join the sorted words with hyphens
    print(sorted_string)



