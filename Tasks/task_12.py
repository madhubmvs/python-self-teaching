#Guessing game
import random
number = random.randint(1, 9)

print(number)
guess_number = int(input('Enter the guessing number' ))
while guess_number != number:
    if guess_number > number:
        print('Number too high')
        guess_number = int(input('Enter the guessing number' ))
    if guess_number < number:
        print('Number too low: ')
        guess_number = int(input('Enter the guessing number '))
    if guess_number == number:
        print('The number is found which is: ' +str(guess_number))


