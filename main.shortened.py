import random

'''
rock: -1
paper: 1
scissor: 0

Rock vs paper: paper wins
Rock vs scissor: Rock wins
paper vs scissor: scissor wins.

In situations where both players choose the same object, the result will be a draw.

'''

computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice : ")
youDict = {"r" : -1, "p" : 1, "s" : 0}
reverseDict = {-1 : "rock", 1 : "paper", 0 : "scissor"}

you = youDict[youstr]

# By now you have two numbers (variables), computer and you

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# if else statement for draw or win\lose

if(computer == you):
    print("Its a draw!")

# shortened and effecient code using pattern 

else:
    if((computer - you) == 1 or (computer - you) == -2):
        print("You win!")

    else:
        print("You lose!")




# nested if elif else ladder or statements

'''
else:
    if(computer == -1 and you == 1): -> (computer - you) = -2
        print("You win!")

    elif(computer == -1 and you == 0): -> (computer - you) = -1
        print("You lose!")

    elif(computer == 1 and you == -1): -> (computer - you) = 2
        print("You lose!")

    elif(computer == 1 and you == 0): -> (computer - you) = 1
        print("You win!")

    elif(computer == 0 and you == 1): -> (computer - you) = -1
        print("You lose!")

    elif(computer == 0 and you == -1): -> (computer - you) = 1
        print("You win!")

    else:
        print("Something went wrong!")

    (There is a pattern for "You win!" and "You lose!" which is "1 and -2" and "2 and -1" respectively)
'''