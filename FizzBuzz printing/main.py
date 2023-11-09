#Joshua Strutton CS160

for number in range(10, 26):

    if number%2 == 0 and number%5 ==0:
            print("FizzBuzz")
    elif number%2 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)
input()