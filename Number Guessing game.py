#This is a simple number guessing game that uses the random module, while loop and if elif else conditional statements. The computer will think of a number between 1 to 100 and you need to try and guess the number in the least number of attempts. The computer will give hints like "Too high" or "Too low" as you start guessing.


import random as r

print("\t*******🎯Welcome to Guess The Number🎯*******\t\n")

start = input("Do you want to start the game (yes/no): ")

while start == "yes":
    num = r.randint(1, 100)
    attempts = 0
    guess = 0
    
    print("\n🤔I'm thinking of a number between 1 and 100🤔\n")
    
    while guess != num:
        guess = int(input("Guess The Number! "))
        if guess > 100:
            print("The range is 0 to 100 😒")
            break
        attempts += 1
        
        if guess > num:
            print("Too High!")
        elif guess < num:
            print("Too Low!")
        else:
            print("You guessed the number in", attempts, "attempts, Congratulations!!🥳🥳\n")
            
            again = input("Do you want to play again? (yes/no): ")
            if again == "yes":
                start = "yes"  
            else:
                start = "no"  
            break

if start == "no":
    print("Awww, maybe next time")

else:
    print("Please enter a valid answer")