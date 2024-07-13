# Initialize a dictionary to store hour counts
hour_counts = {}

# Get the filename from user input (optional)
# filename = input("Enter filename: ")

# Assuming the filename is pre-defined
filename = "messages.txt"  # Replace with your actual filename

try:
  # Open the file for reading
  with open(filename, 'r') as f:
    for line in f:
      # Check if the line starts with "From" (ignoring case)
      if line.lower().startswith("from"):
        # Split the line into words
        words = line.split()
        # Check if there are enough words and extract the time string
        if len(words) >= 6:
          time_string = words[5]
          # Extract the hour from the time string
          colon_pos = time_string.find(':')
          if colon_pos > 0:
            hour = time_string[:colon_pos]
            # Convert hour to integer (optional)
            # hour = int(hour)

            # Update the hour count in the dictionary
            if hour in hour_counts:
              hour_counts[hour] += 1
            else:
              hour_counts[hour] = 1

# Print the hour counts, sorted by hour
for hour, count in sorted(hour_counts.items()):
  print(f"{hour}: {count}")

except FileNotFoundError:
  print(f"Error: File '{filename}' not found.")

