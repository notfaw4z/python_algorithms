def longestWord(word):
  word_list = word.split(" ")
  biggest_word = " "

  for item in word_list:
    if len(item) > len(biggest_word):
      biggest_word = item
  return biggest_word

print(longestWord("I love python!"))
