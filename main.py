import random
import string

from words import data

def get_valid_word(data):
    Word =random.choice(data)
    while '-' in data or ' 'in data:
        Word = random.choice(data)

    return Word.lower()

def hangman():
    Word=get_valid_word(data)
    word_letters=set(Word)
    alphabet= set(string.ascii_lowercase)
    used_letters=set()
    lives=6
    while len(word_letters)>0 and lives>0:
        print('you have ', lives,'lives left and You hav already used that letter :',''.join(used_letters))

        word_list=[letter if letter in used_letters else '-' for letter in Word]
        print('current word', ' '.join(word_list))

        user_letter=input('guess the letter: ').lower()
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print(user_letter,'Letter is not in a word')

        elif user_letter in used_letters:
            print('You have already guessed it!')

        else:
            print('oops !! Wrong letter!')

    if lives==0:
        print('You died!')
        user_letter!=Word
        print('The word was', Word)
    else:
        print('You guessed the word ' , Word)


hangman()



