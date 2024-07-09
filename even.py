def even_numbers(a,b):
    for number in range(a,b+1):
        if number % 2 == 0:
            print(number)
even_numbers(1, 10)

#sorted string
def sort_hyphen(string_list):
    words = string_list.split("-") 
    sorted_words = sorted(words)
    sorted_string = "-".join(sorted_words)
    print(sorted_string)



