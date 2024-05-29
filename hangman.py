from hangman_words import word_list, HANGMANPICS, logo
from random import choice
from replit import clear

print(logo)
print(HANGMANPICS[0])

random_word = choice(word_list)
blank_numbers = len(random_word)
word = ['_' for _ in range(blank_numbers)]
results = ''
        
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
              
p = 1    
while guess_remains > 0:
    try:
       user_guess = input("Enter a word: ")
       if not user_guess.isalpha():
           raise ValueError("You have to enter just words...")
       
    except ValueError as e:
       print(f"Wrong Input!\n{e}")
       if p >= len(HANGMANPICS):
           print(HANGMANPICS[6])
       else:
           print(HANGMANPICS[p]) 
       p += 1 
    else:
        print(f"Hint: it is a {len(random_word)} lenght word")
        print(f"You entered {user_guess} ")
        
        if user_guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == user_guess:
                    word[i] = random_word[i]
                    print(word)
                results = ''.join(word)
                
        else:
            if p >= len(HANGMANPICS):
                print(HANGMANPICS[6])
            else:
                print(HANGMANPICS[p]) 
            p += 1                 
                  
    guess_remains -= 1
    print(f'guess remains: {guess_remains}')
    
    if results == random_word:
        print("You won.")
        break    
    elif guess_remains == 0 and results != random_word:
        print(f"{HANGMANPICS[-1]}\nHe is dead")
        print(f"The word was {random_word}")
        
print(f"You have entered: {results}")    
