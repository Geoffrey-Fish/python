import time
from time import sleep

name = input("Enter your Name: ")

print("Hello, " + name + "!" )
print("Get ready!")

print("")

time.sleep(1)

print("Let us play Hangman!")
time.sleep(0.5)

word = "Flower"

wrd = ''

chance = 10

while chance > 0 :
    failed = 0
    for char in word :
        if char in wrd :
            print(char)
        else :
            print("_")
            failed += 1
    if failed == 0:
        print("You won!!! Congrats!")
        break
    guess = input("Guess a Letter: ")
    wrd += guess
    if guess not in word:
        chance -= 1
        print("Wrong Guess! Try again.")
        print("You have",+ chance,"turns left.")
        if chance == 0 :
            print("You Lose! Better luck next time.")