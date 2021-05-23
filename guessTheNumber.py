import random

n = random.randint(10,99)

guess = 5
print('Guess the number\nHINT: The number is of 2 digits')

while True:
    a = int(input('Enter the number: '))
    if guess != 0:

        if a>n:
            print('Decrease your number!!')
            guess -= 1
            print('Number of guesses left =', guess)
            continue
        elif a<n:
            print('Increase your number')
            guess -= 1
            print('Number of guesses left =', guess)
            continue

        else:
            print('Congratulations, You got it right!!')
            break

    else:
        print('Number of guesses left = 0')
        print('The number was', n)
        print('You lost, Better Luck next time!!')
        break
