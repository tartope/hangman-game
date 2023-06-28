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
    num_tries = 7
    if num_tries == 0: 
        print("Game over") 
        return
    if guess in word:
        while num_tries > 1 and num_tries <=7:
            print("Good guess")
            print(HANGMAN_PICS[0]) 
            num_tries -= 1
            print(f"Tries left: {num_tries}")
            another_guess = input("Guess again: ")
            # game_board(another_guess)
    # else:
    #     print("Oops! That is not correct.")

game_board(guess)

# Comment