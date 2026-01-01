import sys

from stats import count_chars, count_words, sort_chars_by_frequency

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def usage():
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

def main():
  if len(sys.argv) != 2:
    usage()

  book_pathname = sys.argv[1]
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_pathname}...")
  print("----------- Word Count ----------")
  frankenstein = get_book_text(book_pathname)
  print(f"Found {count_words(frankenstein)} total words")

  print("--------- Character Count -------")
  chars_and_frequency = sort_chars_by_frequency(count_chars(frankenstein))
  for i in range(0,len(chars_and_frequency)):
    char = chars_and_frequency[i]["char"]
    num = chars_and_frequency[i]["num"]
    if not char.isalpha():
      continue
    print(f"{char}: {num}")

  print("============= END ===============")

  return None

main()
