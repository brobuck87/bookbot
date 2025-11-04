from stats import count_words, count_instances_of_characters, print_report
import sys

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
  with open(filepath, "r") as file:
    return file.read()

def count_words(text):
  return len(text.split())

def main():
  print(f"============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print(f"----------- Word Count ----------")
  print(f"Found {count_words(get_book_text(filepath))} total words")
  print(f"--------- Character Count -------")
  print_report(count_instances_of_characters(get_book_text(filepath)))
  print(f"============= END ===============")


main()