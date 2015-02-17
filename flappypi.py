#####
# TODO
#####

from collections import deque
from random import randint
import time
import thread
import unicornhat as UH

#####
# Global variables
#####

playField = deque()
advanceCounter = 0
gapCounter = 0
score = 0
birdHeight = 4
birdMoves = deque()

#####
# Set the playfield to blank
#####
def clearPlayField():
	global playField

	playField = deque()
	for n in range(8):
		playField.append([0, 0, 0, 0, 0, 0, 0, 0])

	UH.clear()

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
# Display the playfield and run scoring / collision logic
#####
def renderPlayField():
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
				UH.set_pixel(m, n, 255, 0, 0)

				# Adjust bird height
				print birdMoves
			else:
				# This line doesn't have the bird on
				playFieldLine.append(playField[m][n])
				UH.set_pixel(m, n, 0, 255 * playField[m][n], 0)

		print playFieldLine
		UH.show()

	print "------------------------"


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
#
#####
def waitForInput():
	while True:
		choice = raw_input("")
		if (choice == ""):
			break

#####
# TODO
#####
def inputThread(l):
	raw_input()
	l.append(None)

#####
# Wait for a player to come and start a game
#####
def waitForPlayer():
	showFrameOne = True
	screen = []
	l = []

	frameOne = [[ 0, 0, 0, 1, 1, 0, 0, 0 ],
	            [ 0, 0, 0, 1, 1, 0, 0, 0 ],
	            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
	            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
	            [ 0, 0, 1, 1, 1, 1, 0, 0 ],
	            [ 0, 0, 1, 1, 1, 1, 0, 0 ],
	            [ 0, 1, 1, 1, 1, 1, 1, 0 ],
	            [ 0, 0, 0, 0, 0, 0, 0, 0 ]
	           ]

	frameTwo = [[ 0, 0, 0, 1, 1, 0, 0, 0 ],
	            [ 0, 0, 0, 1, 1, 0, 0, 0 ],
	            [ 0, 0, 0, 1, 1, 0, 0, 0 ],
	            [ 0, 0, 0, 1, 1, 0, 0, 0 ],
	            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
	            [ 0, 0, 1, 1, 1, 1, 0, 0 ],
	            [ 0, 1, 1, 1, 1, 1, 1, 0 ],
	            [ 0, 0, 0, 0, 0, 0, 0, 0 ]
	           ]

	thread.start_new_thread(inputThread, (l,))

	while True:	
		if l:
			break

		if (showFrameOne):
			screen = frameOne
		else:
			screen = frameTwo

		showFrameOne = not showFrameOne

		for y in range(8):
			for x in range(8):
				r = screen[y][x] * 255
				UH.set_pixel(x, y, r, 0, 0)

		UH.show()

		for n in range(8):
			print screen[n]

		print "------------------------"
		time.sleep(1)

#####
# Game ended, display score and end screen
#####
def gameEnded():
	print "GAME OVER (SCORE " + str(score) + ")"
	time.sleep(10)

#####
# Flap the wing
#####
def flap():
	global birdMoves
	print "FLAP"
	birdMoves.append(1)
	birdMoves.append(1)

#####
# Deal with a movement where there was no flap
#####
def noFlap():
	global birdMoves
	print "NO FLAP"
	birdMoves.append(-1)

#####
# TODO
#####
def playGame():
	global gameOver
	global score
	global birdHeight

	l = []
	score = 0
	birdHeight = 4
	gameOver = False

	clearPlayField()
	thread.start_new_thread(inputThread, (l,))

	# Start with a flap to get the user going
	flap()
	
	while (not gameOver):
		renderPlayField()
		advancePlayField()
		if (l):
			flap()
			l = []
			thread.start_new_thread(inputThread, (l,))
		else:
			noFlap()

		time.sleep(2)

#####
# Entry point, main loop
#####
while (True):
	waitForPlayer()
	playGame()
	gameEnded()
