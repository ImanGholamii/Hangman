from hangman_words import word_list, HANGMANPICS, logo
from random import choice

print(logo)
print(HANGMANPICS[0])

# random_word = choice(word_list)
random_word = 'abaaas'
blank_numbers = len(random_word)
word = []
for number in range(blank_numbers):
        word += '_'
        
guess_remains = [4, 6, 8] # To select the difficulty by the user

difficulty_level = input("Select the difficulty level:\n1)easy(8 guesses)\n2)normal(6 guesses)\n3)hard(4 guesses)\n>>> ")

if difficulty_level == '1' or difficulty_level.lower() == 'easy':
    guess_remains = 8
    print(f"difficulty level: Easy\nremaining guesses: {guess_remains}")
elif difficulty_level == '2' or difficulty_level.lower() == 'normal':
    guess_remains = 6
    print(f"difficulty level: Normal\nremaining guesses: {guess_remains}")
elif difficulty_level == '3' or difficulty_level.lower() == 'hard':
    guess_remains = 4
    print(f"difficulty level: Hard\nremaining guesses: {guess_remains}")
else:
    print("⚠️  Invalid Input.\n🔄 Restart the game and enter '1' or 'easy' and so on...")



        
print(word)
print(type(word))        
print(random_word)
w = 'a'

for i in range(len(random_word)):
    if random_word[i] == w:
        word[i] = random_word[i]
        
print(word)               
    
# while guess_remains >= 0:
#     try:
#        user_guess = str(input("Enter a word: "))
#     except TypeError:
#        print("Wrong Input!\nYou have to enter just words...") 
    