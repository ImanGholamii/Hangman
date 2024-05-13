from Day_007_hangman_words import word_list, HANGMANPICS, logo
from random import choice

print(logo)
print(HANGMANPICS[0])

random_word = choice(word_list)
black_numbers = len(random_word)
guess_remains = len(random_word)
