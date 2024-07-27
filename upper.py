filename = input("Enter the filename: ")

try:
  with open(filename, 'r') as file:
    for line in file:
      print(line.upper().rstrip())
except FileNotFoundError:
  print(f"Error: File '{filename}' not found.")
