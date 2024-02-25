def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  #print(text)
  print(num_words)
  letters = get_letter_count(text)
  print(letters)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
  return len(text.split())

def get_letter_count(text):
  letters = {}
  words = text.split()
  for word in words:
    lowered_word = word.lower()
    for letter in lowered_word:
      if letter in letters:
        letters[letter] += 1
      else:
        letters[letter] = 1
  
  return letters
    
main()
