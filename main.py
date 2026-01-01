from stats import count_chars, count_words, sort_chars_by_frequency

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main():
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  frankenstein = get_book_text("books/frankenstein.txt")
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
