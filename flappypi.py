#####
# TODO
#####

from collections import deque
from random import randint
import time

playField = deque()
advanceCounter = 0
gapCounter = 0

#####
# Set the playfield to blank
#####
def clearPlayField():
	global playField

	playField = deque()
	for n in range(8):
		playField.append([0, 0, 0, 0, 0, 0, 0, 0])

#####
# Generate a new pipe represented as 8 on or off states
# with a 3 LED gap for the bird to fly through
#####
def generatePipe():
	gapStart = randint(0, 4)
	newPipe = []

	for n in range(8):
		if (n < gapStart) or (n > gapStart + 2):
			newPipe.append(1)
		else: 
			newPipe.append(0)

	return newPipe

#####
# Generate a blank line to go between pipes
#####
def generatePipeGap():
	return [ 0, 0, 0, 0, 0, 0, 0, 0 ]

#####
# TODO
#####
def printPlayField():
	global score
	global gameOver

	for n in range(8):
		playFieldLine = []
		for m in range(8):
			if (n == birdHeight and m == 2):
				# This is the line with the bird on, do some checks
				if (playField[m][n] == 1):
					# Player collided with a pipe!
					gameOver = True
				elif (sum(playField[m]) > 0):
					score += 1
					print "SCORE (" + str(score) + ")"

				# Render the bird
				playFieldLine.append(2)
			else:
				# This line doesn't have the bird on
				playFieldLine.append(playField[m][n])

		print playFieldLine

#####
# Handles side scrolling the play field
#####
def advancePlayField():
	global advanceCounter, gapCounter
	
	if (advanceCounter < 5):
		# For now do nothing user is on lead in to
		# first pipe
		advanceCounter += 1
	else:
		if (advanceCounter == 5):
			# First pipe
			playField.popleft()
			playField.append(generatePipe())
			advanceCounter += 1
		else:
			playField.popleft()
			if (gapCounter == 3):
				playField.append(generatePipe())
				gapCounter = 0
			else:
				playField.append(generatePipeGap())
				gapCounter += 1

#####
# TODO
#####
def waitForPlayer():
	print "TODO: Start screen!"

#####
# TODO
#####
def doGameOver():
	print "GAME OVER (SCORE " + str(score) + ")"

#####
# TODO
#####
def playGame():
	global gameOver
	global score
	global birdHeight

	clearPlayField()
	score = 0
	birdHeight = 4
	gameOver = False

	while (not gameOver):
		printPlayField()
		print "------------------------"
		advancePlayField()
		time.sleep(2)

#####
# TODO
#####
while (True):
	waitForPlayer()
	playGame()
	doGameOver()