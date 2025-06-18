import random
from wordsHangman import words
import string 

def get_valid_word():
    word = random.choice(words) #Chooses a random word from the list(in the argument)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():

    #letters used
    # " ".join(['a', 'b', 'cd']) --> 'a b cd'
    
    
    word = get_valid_word()
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed 

    lives = len(word) * 2

    #what the current word is (ie. W _ R D)
    
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. ", "You have used the following letters: ", " ".join(used_letters))
        
        word_list = [letter if letter in used_letters else "_" for letter in word ]   #Why for i in word: if i in used_letter: print("i", end = " ") else: print("_")
        print("The Current word is: ", " ".join(word_list))


        user_letter = input("\n Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 
                print("Oops! The letter is NOT in the word!!")
    
        elif user_letter in used_letters:
            print(f"You have already used the letter {user_letter}. Try again!")
        else:
            print("Invalid Character. Please try again!")

    if lives == 0:
        print(f"Sorry. You have died. You lost. The word is {word}")
    else:
        print(f"Congrats!! You guessed the word {word} correctly")
     
hangman()