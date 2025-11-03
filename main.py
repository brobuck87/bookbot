def get_book_text(filepath):
  with open(filepath, "r") as file:
    return file.read()

def count_words(text):
  return len(text.split())

def main():
  print(f"Found {count_words(get_book_text('books/frankenstein.txt'))} total words")

main()