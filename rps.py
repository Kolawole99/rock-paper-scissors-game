from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    
    #Checks if player input is the same as computer
    if player == computer:
        print("Tie!")
    
    #Checks for player being rock
    elif player == "Rock":
        #Determines winnners if paper is computer
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        #Determines winner if scissors is computer
        else:
            print("You win!", player, "smashes", computer)
    
    #Checks for player being paper
    elif player == "Paper":
        #Determines winner if computer is scissors
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        #Determines winner if computer is rock
        else:
            print("You win!", player, "covers", computer)
    
    #Checks for player being scissors
    elif player == "Scissors":
        #Determines winner if computer is rock
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        #Determines winner if computer is paper
        else:
            print("You win!", player, "cut", computer)
    
    #Handles anything outside Rock, Paper and Scissors as an error
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]