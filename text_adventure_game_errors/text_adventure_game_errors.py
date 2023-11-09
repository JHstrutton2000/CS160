# CS160 Fall 2020 Final Project
# Name: Joshua Strutton
# Date: 3/16/23

# 1 import the random module
import math
import random

lives = 5
won = 0

pathText = "Do you wish to return to path? (Yes/No)"

# 2 Got rid of extra parentheses, also moved .lower().strip() onto variable declaration to save processing time later (prevents running those methods every time later)
answer = input("Do you want to go on an adventure? (Yes/No) ").lower().strip()
    

#num = 1 #debug line

# hint: the program should convert player's input to lowercase and get rid of any space player enters
# hint: check out what .upper(), .lower(), .strip() do on a string, reference: https://www.w3schools.com/python/python_ref_string.asp
# 3 switched from upper to lower
if answer == "yes":
    while lives > 0:
        print("you have {} lives.".format(lives))

        # hint: pay attention to the variable name
        # 4 Variable names need to be the same charactrs, you just created a new variable.
        answer = input("You are lost in the forest and the path splits. Do you go left or right? (Left/Right) ").lower().strip()
        if answer == "left":
            # 5 fix the indent, python cars about indents. Its how the language tracks whats within the scope.
            answer = input("An evil witch tries to cast a spell on you, do you run or attack? (Run/Attack) ").lower().strip()
            if answer == "attack":
                print("She turned you into a green one-legged chicken, you lost!")
                lives -= 1
                if input(pathText).lower().strip() != "yes":
                    break
            # 6 to check if two things are equal you need == not =
            elif answer == "run":
                print("Wise choice, you made it away safely.")
                answer = input("You see a car and a plane.  Which would you like to take? (Car/Plane) ").lower().strip()
                if answer == "plane":
                    print("Unfortunately, there is no pilot. You are stuck!")
                    if input(pathText).lower().strip() != "yes":
                        break
                elif answer == "car":
                    print("You found your way home. Congrats, you won!")
                # 7 else is used for any situation not caught by the original conditional, you wanted an elif which allows you to add on another conditional.
                elif answer != "plane" or answer != "car":
                    print("You spent too much time deciding...")
                    if input(pathText).lower().strip() != "yes":
                        break
            else:
                print("You are frozen and can't talk for 100 years...")
                lives -=1
                if input(pathText).lower().strip() != "yes":
                    break
        elif answer == "right":
            # hint: the program should randomly generate a number in betwwen 1 and 3 (including 1 and 3)
            # hint: remember random module? reference: https://www.w3schools.com/python/module_random.asp
            # 8 the range is wrong, it should be 1 to 3 not 0 to 3, this will include 0
            num = random.randint(1,3)
            
            # 9 you need to cast the input from a string to a float.
            answer = float(input("Pick a number from 1 to 3: ").lower().strip())
            # hint: will the following if statment ever be executed even when the values of answer and num are the same? If not, can you fix the problem?
            # hint: the error is not necessarily in the line below.
            
            if answer == num:
                print("I'm also thinking about {}".format(num))
                print("You woke up from this dream.")
                won = 1
                break
            else:
                print("You fall into deep sand and get swallowed up. You lost!")
                lives -= 1
                if input(pathText).lower().strip() != "yes":
                    break
        else:
            print("You can't run away...")
            if input(pathText).lower().strip() != "yes":
                break    
    if won == 0:
        print("Game Over!")
# 10
else:
    print("That's too bad!")
    won = 1

input("Press any button to exit")


