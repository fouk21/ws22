import random
import subprocess

def commands():
    return True

def guessingGame():
    print("GUESSING GAME: GUESS THE NUMBER")
    number  = random.randint(1,10)
    print(number)
    tries = 3
    win = False
    while tries > 0:
        guess = int(input("Guess what number i am thinking: "))
        if number == guess:
            print("Congratulations!")
            win = True
            break
        tries -= 1
        print("Sorry wrong guess, " + str(tries) + " left")
    if not win:
        print("You lost")

if __name__ == '__main__':
    guessingGame()
    #print("hello world")
