def count_words(text):
  return len(text.split())

def count_chars(text):
  lower_text = text.lower()
  counts_by_character = {}
  for char in lower_text:
    if char not in counts_by_character:
      counts_by_character[char] = 1
    else:
      counts_by_character[char] += 1
  
  return counts_by_character

def sort_on(items):
  return items["num"]

def sort_chars_by_frequency(chars_and_counts):
  chars_by_frequency = []
  for char_count in chars_and_counts:
    char_and_num = { 
      "char" : char_count,
      "num" :  chars_and_counts[char_count]
    }
    chars_by_frequency.append(char_and_num)

  chars_by_frequency.sort(reverse=True, key=sort_on)
  
  return chars_by_frequency
