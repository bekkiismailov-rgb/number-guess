import random

topRange = input('Type a number: ')

if topRange.isdigit():
    topRange = int(topRange)
else:
    print('Please type a number next time')
    quit()

r = random.randint(0, topRange)
guesses = 0
print(r)  

while True:
    guesses += 1
    userGuess = input("Make a guess: ")

    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print('Please type a number')
        continue

    if userGuess == r:
        print('You got it!')
        break
    else:
       if userGuess > r:
           print('You were above the number')
       else:
           print('You were below the number')
        
print('You got ', guesses)