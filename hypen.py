def sort_hyphen(string_list):
    words = string_list.split("-")
    sorted_words = sorted(words)
    sorted_string = "-".join(sorted_words)
    print(sorted_string)


