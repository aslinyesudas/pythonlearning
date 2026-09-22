# hangman in python
import random

words = ("apple", "orange", "banana", "coconut", "pinepple")

#dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "  ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(hint))
    

def main():

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or nor guess.isalpha():
        print("Invalid input")
        continue

    if guess in guessed_letters:
        print(f"{guess} is already guessed")
        continue

    guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
        
    
        
        

if __name__ == '__main__':
    main()
