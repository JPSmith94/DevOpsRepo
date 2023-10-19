#input_word = input("Enter a Word")
#vowels = ["a","e","i","o","u"]
#vowel_count = 0
#for i in range(len(input_word)):
  #  if input_word[i] in vowels:
 #       vowel_count += 1
#
#print(f"Your word has {vowel_count} vowels in it")


word = input("Enter a word: ")

counter = 0
vowel_counter = 0

while counter < len(word):
    x = word[counter]
    if x in "aeiou":
        vowel_counter += 1
    counter += 1
print(f"Number of vowels in {word} is {vowel_counter}")