high = 100
low = 0
guess = (high + low)/2
print('Please think of a number between 0 and 100!')
print('Is your secret number ', guess, "?")
answer = input("Enter 'h' to indicat the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly.: "  )
while answer != 'c':
    if answer == 'c':
         print('Game over. Your secret number was ', int(guess))
    elif answer =='h':
         high = guess
         guess = (guess + low)/2
         print('Is your secret number ', int(guess))
         answer = input("Enter 'h' to indicat the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly.: "  )
    else:
        low = guess
        guess = (high + guess)/2
        print("Is your secret number ", int(guess))
        answer = input("Enter 'h' to indicat the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly.: "  )

print('Game over. Your secret number was ', int(guess))

