# Andrew Ellis
# STAT 1129
# Final Project Option 3 - Rock, Paper, Scissors, Shoot Game

import random
from random import randint

start = True
playAgain = False

playerScore = 0
computerScore = 0

gameMoves = ["R", "P", "S"]

def getRandomMove():
	return random.choice(gameMoves)

def isValid(playerMove):
	if playerMove in gameMoves:
		return True
	else:
		return False

def showResult(playerMove, computerMove):
	outcome = ""

	if isValid(playerMove) and isValid(computerMove):
	    
		if playerMove == computerMove:
			print("Same Move!\nYou Tied!")
		# Rock v Paper - You Lose
		elif playerMove == gameMoves[0] and computerMove == gameMoves[1]:
		    print("Rock v Paper\nYou Lose!")
		    updateScore(1)
		# Rock v Scissor - You Win
		elif playerMove == gameMoves[0] and computerMove == gameMoves[2]:
		    print("Rock v Scissor\nYou Win!")
		    updateScore(0)
		# Paper v Rock - You Win
		elif playerMove == gameMoves[1] and computerMove == gameMoves[0]:
		    print("Paper v Rock\nYou Win!")
		    updateScore(0)
		# Paper v Scissor - You Lose
		elif playerMove == gameMoves[1] and computerMove == gameMoves[2]:
		    print("Paper v Scissor\nYou Lose!")
		    updateScore(1)
		# Scissor v Rock - You Lose
		elif playerMove == gameMoves[2] and computerMove == gameMoves[0]:
		    print("Scissor v Rock\nYou Lose!")
		    updateScore(1)
		# Scissors v Paper - You Win
		elif playerMove == gameMoves[2] and computerMove == gameMoves[1]:
		    print("Scissor v Paper\nYou Win!")
		    updateScore(0)

def updateScore(winner):
    global playerScore
    global computerScore
    global start
    
    if winner == 0:
        playerScore += 1
    else:
       computerScore += 1
    
    print("| Player: %d | Computer: %d | \n" % (playerScore, computerScore))

    userPlayAgain = input("Play again? (Y/N): ")
    while userPlayAgain != 'Y' and userPlayAgain != 'N':
        userPlayAgain = input("Play again? (Y/N): ")

    if userPlayAgain == 'Y':
        start = True
    else:
        start = False
        
        
def main():
    while start == True:
    	playerMove = input("Enter your move (R, P, S): ")
    	computerMove = getRandomMove()
    	showResult(playerMove, computerMove)

if __name__ == "__main__":
    main()
