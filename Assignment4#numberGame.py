#import from Python libraries
import random

#set the lower bound value to 1
low=1

print('Welcome to my guessing game! :)')

#create a loop to make sure the user inputs an appropriate value 
hi=0
while hi<10:
    try:
        hi=int(input('Please enter a value greater than or equal to 10:'))

    except ValueError:
        print('You must enter an integer value greater than or equal to 10.')

#compute a random value between 1 and the value entered by the user    
a=int(random.randint(low, hi))
print('I computed a random number between 1 and ', hi,'. Can you guess what it is?')

#create a loop to continually ask the user to guess the computed random value
while hi>=10:

    try:
        b=int(input("Please enter a guess:"))
    
    except ValueError:
        print("Please enter an integer value.")
        continue

    if b<a:
        print("Your value is too low. Try again!")
        continue

    if b>a:
        print("Your value is too high. Try again!")
        continue

    if b==a:
        print('Congratulations! You guessed it! The value was:', a,  '\nGood Bye! :)' )
        quit()
