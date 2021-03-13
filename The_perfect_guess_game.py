import random
randomNo=random.randint(1,100)
guesses=0
userGuess=None


while(userGuess!=randomNo):
    userGuess=int(input("enter your guess:"))
    guesses+=1
    if(userGuess==randomNo):
        print("You guessed it right!")
    else:
        if(userGuess>randomNo):
            print("You guesses it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")    
   

print(f"You guessed the number in {guesses} guesses")

