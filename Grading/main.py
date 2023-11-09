#Joshua Strutton CS160

print("Enter your Grade Score: ")

Grade = input()

print(Grade)

letter = 'F'

if int(Grade) >= 90:
    letter = 'A'
elif int(Grade) >= 80:
    letter = 'B'
elif int(Grade) >= 70:
    letter = 'C'
elif int(Grade) >= 60:
    letter = 'D'

print("your grade is : " +letter)

print("Press a key to close")
input()