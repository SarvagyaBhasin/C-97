import random
compnum = random.randint(1,15)
chances = 0
print ("Welcome to the number Guessing game, get ready to test your luck")
while chances<5 :
    guess= int(input ("Enter your guess: "))

    if guess == compnum :
        print ("Congratulations!! You guessed it!!")
        break
    
    elif guess < compnum :
        print ("Hard Luck, you'll have to guess higher than this")

    else : 
        print ("Hard Luck, you'll have to guess lower than this")
    chances += 1
if not chances < 5:
    print ("You lose, better lucknexet time")