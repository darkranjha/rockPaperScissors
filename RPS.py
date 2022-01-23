# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 09:29:28 2022

@author: Rahulinder Dhillon CEIS 110 
Rock Paper Scissors Game! 
"""

#import random module
import random

#initialize variables

playerDecision = ""
computerDecision = ""
playerScore = 0
computerScore = 0
keepPlaying = True

#Function to randomly get computer decision for what they want to throw
def getComputerDecision():
    #get random int 0-2. 0 = rock, 1=paper, 2=scissors
    ranCompDecision = random.randint(0,2)
    #print ("This is int value of ranCompDecision " , str(ranCompDecision)) #debuggin purposes
    if (ranCompDecision==0):
       return "Rock"
    elif (ranCompDecision==1):
       return "Paper"
    elif (ranCompDecision==2):
       return "Scissors"
    else: #we should have only gotten a value 0-2, if not something went wrong and let's exit out of program
       print ("Somthing went wrong, please contact Rohan @ 614-649-1530")
       raise SystemExit
       #exit() doesn't work, got NameError.. Maybe have to import a module?

def determineWinner(playerChoice,computerChoice):
    if (playerChoice == computerChoice):
        return "Tie"
    elif (playerChoice == "ROCK" and computerChoice == "SCISSORS"):
        return "Player"
    elif (playerChoice == "ROCK" and computerChoice == "PAPER"):
        return "Computer"
    elif (playerChoice == "PAPER" and computerChoice == "ROCK"):
        return "Player"
    elif (playerChoice == "PAPER" and computerChoice == "SCISSORS"):
        return "Computer"
    elif (playerChoice == "SCISSORS" and computerChoice == "PAPER"):
        return "Player"
    elif (playerChoice == "SCISSORS" and computerChoice == "ROCK"):
        return "Computer"
    
    
       
#loop to start the game
while (keepPlaying == True):
    playerDecision = input("Please type in Rock, Paper, Scisscors, or Q to quit ")     
    #print(playerDecision.upper()) #debugging purposes
    
    # Check what the user input and play the game
    if (playerDecision.upper()=="Q" or playerDecision.upper()=="ROCK" or playerDecision.upper()=="PAPER" or playerDecision.upper()=="SCISSORS"):
        #print("Good selection")
        if (playerDecision.upper()=="Q"): #User doesn't want to play anymore
            keepPlaying=False
        else: #User selected either rock, paper, or scissors
            computerDecision = getComputerDecision()
            winner = determineWinner(playerDecision.upper(),computerDecision.upper())
            print("You picked " + playerDecision + " and the computer picked " + computerDecision)
            if (winner == "Tie"):
                print("The result is a tie, score unchanged. Player - ", str(playerScore), "and Computer - ",str(computerScore))
            elif (winner == "Player"):
                playerScore+=1
                print(playerDecision + " beats " + computerDecision + "!")
                print("Player wins! Player - ", str(playerScore), "and Computer - ",str(computerScore))
            elif (winner == "Computer"):
                computerScore+=1
                print(computerDecision + " beats " + playerDecision + "!")
                print("Computer wins! Player - ", str(playerScore), "and Computer - ",str(computerScore))
    else:
        print("You have entered an invalid selection, please try again")
    
    


   