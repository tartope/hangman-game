word = "ant"

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
    ===''', '''
    +---+
    O   |
        | 
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
    ===''']


guess = input("Guess the letter: ")

def num_of_tries(attempts):
    max = 7
    
    while attempts <= 7:
        max -=1
    pass


def game_board(guess): 
               
    if guess in word:
        print("Good guess")
        print(HANGMAN_PICS[0]) 
        another_guess = input("Guess again: ")
        game_board(another_guess)
    # else:
    #     print("Oops! That is not correct.")

game_board(guess)

# Comment