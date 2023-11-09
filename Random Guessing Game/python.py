#Joshua Strutton CS160

import random

print("Guessing a number between 1 and 10:")

running = 1
rand = random.randint(1, 10)
while running==1:
    print("Guess your number")
    guess = int(input())
    if guess == rand:
        print("You guessed correctly")
        running = 0
    elif guess > rand:
      print("Your guess is too high!")
    elif guess < rand:
      print("Your guess is too low.")
      
      
input()