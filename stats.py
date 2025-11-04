def count_words(text):
  return len(text.split())

def count_instances_of_characters(text):
  # split the text into a list of characters 
  # lower case the characters to avoid case sensitivity
  # count the occurrences of each character
  counts = {}
  for char in text.lower():  # No need for list() - strings are iterable
    counts[char] = counts.get(char, 0) + 1
  return counts

def print_report(counts):
  # Sort once before the loop
  sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)
  for char, count in sorted_chars:
    if char.isalpha():
      print(f"{char}: {count}")