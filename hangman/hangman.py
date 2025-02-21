import random
import string
from words import words

def get_valid_word(words):          # This function will return a random word 
    word = random.choice(words)     # from the list of words without a '-' or ' ' in it
    
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():                          # This is the main function to run hangman game
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    
    HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
    
    # while not all letters have been guessed
    while len(word_letters) > 0 and lives > 0:
        
        print(HANGMANPICS[lives])
        
        print('Guessed letters: ', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print('Answer: ', ' '.join(word_list))
       
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:      # If the user's letter is in the alphabet and not in the used letters
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:               # If the user's letter is in the used letters
            print('You have already used that character. Please try another letter.')
    
    if lives == 0:
        print('You have died! The word was: ', word)
    else:
        print('You guessed the word: ', word, '!!')

hangman()