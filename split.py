def extract_unique_words(filename):

  unique_words = []

  with open(filename, 'r') as file:
    for line in file:
      words = line.split()
      for word in words:
        if word not in unique_words:
          unique_words.append(word)

  unique_words.sort()
  print(unique_words)  


if __name__ == "__main__":
  filename = input("Enter the filename: ")
  extract_unique_words(filename)
