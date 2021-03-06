#####
# Filename:    flappypigpio.py
# Description: Flappy bird type game in Python for Pimoroni Unicorn Hat
#              Uses 2 buttons connected to GPIO 19 (start) and 6 (flap)
# Author:      Simon Prickett
#####

from collections import deque
from random import randint
import time
import thread
import unicornhat as UH
import RPi.GPIO as GPIO

#####
# Global variables
#####

playField = deque()
advanceCounter = 0
gapCounter = 0
score = 0
birdHeight = 4
birdMoves = deque()
startPressed = False
flapPressed = False

#####
# Button press callback
#####
def buttonPressed(gpioPinNumber):
	global startPressed
	global flapPressed

	if (gpioPinNumber == 6):
		flapPressed = True
	else:
		if (gpioPinNumber == 19):
			startPressed = True

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

				# Render the bird
				playFieldLine.append(2)
				UH.set_pixel(m, n, 255, 0, 0)
			else:
				# This line doesn't have the bird on
				playFieldLine.append(playField[m][n])
				if (m <= 2):
					pipeRColor = 0
					pipeGColor = 255
				else:
					pipeRColor = 238
					pipeGColor = 238

				UH.set_pixel(m, n, pipeRColor * playField[m][n], pipeGColor * playField[m][n], 0)

		UH.show()

#####
# Handles side scrolling the play field
#####
def advancePlayField():
	global advanceCounter, gapCounter, birdHeight, birdMoves
	
	birdHeight += birdMoves.popleft()
	if (birdHeight < 0):
		# Bird can't go any higher than top of screen
		birdHeight = 0
	elif (birdHeight > 8):
		# Bird can't go any lower than bottom of screen
		birdHeight = 8 

	if (advanceCounter < 5):
		# For now do nothing user is on lead in to
		# first pipe
		advanceCounter += 1
	else:
		playField.popleft()

		if (advanceCounter == 5):
			# First pipe
			playField.append(generatePipe())
			advanceCounter += 1
		else:
			# Draw a pipe every 7th frame
			if (gapCounter == 7):
				playField.append(generatePipe())
				gapCounter = 0
			else:
				playField.append(generatePipeGap())
				gapCounter += 1

#####
# Wait for a player to come and start a game, alternate 
# between two images simulating pressing of a button
#####
def waitForPlayer():
	global startPressed

	startPressed = False
	GPIO.add_event_detect(19, GPIO.FALLING, buttonPressed, bouncetime=1000)
	showFrameOne = True
	screen = []

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

	while (not startPressed):	
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

		time.sleep(1)
	
	GPIO.remove_event_detect(19)

#####
# Game ended, display score and end screen
#####
def gameEnded():
	if (score == 0):
		# Render a big 0
		screen = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
			  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
			  [ 0, 0, 1, 0, 0, 1, 0, 0 ],
			  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
			  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
			  [ 0, 0, 1, 0, 0, 1, 0, 0 ],
			  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
			  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
		       ]
	
		for y in range(8):	
			for x in range(8):
				g = screen[y][x] * 255
				UH.set_pixel(x, y, 0, g, 0)

		UH.show()
	else:
		# Render one dot per point scored
		x = 0
		y = 0

		UH.clear()
		UH.show()

		for n in range(score):
			UH.set_pixel(x, y, 0, 255, 0)
			UH.show()
			time.sleep(0.5)
			x+=1 
			if (x == 8):
				y+= 1
				x = 0

			if (y == 8):
				break

	time.sleep(5)

#####
# Flap the wing
#####
def flap():
	global birdMoves
	birdMoves = deque()
	birdMoves.append(-1)
	birdMoves.append(-1)

#####
# Deal with a movement where there was no flap
#####
def noFlap():
	global birdMoves
	birdMoves.append(1)

#####
# Play an instance of the game
#####
def playGame():
	global gameOver
	global score
	global birdHeight
	global flapPressed

	score = 0
	birdHeight = 4
	gameOver = False
	flapPressed = False

	GPIO.add_event_detect(6, GPIO.FALLING, buttonPressed, bouncetime=200)
	clearPlayField()

	# Start with a flap to get the user going
	flap()
	
	while (not gameOver):
		if (flapPressed):
			flap()
			flapPressed = False
		else:
			noFlap()

		renderPlayField()
		advancePlayField()

		# Check for collision with floor
		if (birdHeight == 8):
			gameOver = True

		# Speed up after 10th and 20th pipes
		if (score < 10):
			sleepTime = 0.2
		elif (score < 20):
			sleepTime = 0.15
		else:
			sleepTime = 0.1

		time.sleep(sleepTime)

	GPIO.remove_event_detect(6)

#####
# Hardware setup
#####

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#####
# Entry point, main loop
#####
while (True):
	waitForPlayer()
	playGame()
	gameEnded()
