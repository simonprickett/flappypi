import RPi.GPIO as GPIO
import unicornhat as UH
import time

def paintLEDs(patternToPaint):
	for y in range(8):
		for x in range(8):
			r = patternToPaint[y][x] * 255
			UH.set_pixel(x, y, r, 0, 0)
	UH.show()

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	right_button = GPIO.input(19)
	left_button = GPIO.input(6)
	up_button = GPIO.input(5) 
	down_button = GPIO.input(13)

	if right_button == False:
		print "5"
	if left_button == False:
		print "6"
	if up_button == False:
		print "19"
	if down_button == False:
		print "13"

	patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                          [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                          [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                          [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                          [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                          [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                          [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                          [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                        ]

	if right_button == False:
		print "RIGHT"
		patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
       		                  [ 0, 0, 0, 0, 1, 0, 0, 0 ],
                       		  [ 0, 0, 0, 0, 0, 1, 0, 0 ],
                                  [ 0, 1, 1, 1, 1, 1, 1, 0 ],
                                  [ 0, 1, 1, 1, 1, 1, 1, 0 ],
                                  [ 0, 0, 0, 0, 0, 1, 0, 0 ],
                                  [ 0, 0, 0, 0, 1, 0, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                ]
	if left_button == False:
		print "LEFT"
		patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
       		                  [ 0, 0, 0, 1, 0, 0, 0, 0 ],
                       		  [ 0, 0, 1, 0, 0, 0, 0, 0 ],
                                  [ 0, 1, 1, 1, 1, 1, 1, 0 ],
                                  [ 0, 1, 1, 1, 1, 1, 1, 0 ],
                                  [ 0, 0, 1, 0, 0, 0, 0, 0 ],
                                  [ 0, 0, 0, 1, 0, 0, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                ]
	if up_button == False:
		print "UP"
		patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
       		                  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                       		  [ 0, 0, 1, 1, 1, 1, 0, 0 ],
                                  [ 0, 1, 0, 1, 1, 0, 1, 0 ],
                                  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                                  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                                  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                ]
	if down_button == False:
		print "DOWN"
		patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
       		                  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                       		  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                                  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                                  [ 0, 1, 0, 1, 1, 0, 1, 0 ],
                                  [ 0, 0, 1, 1, 1, 1, 0, 0 ],
                                  [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                ]

	paintLEDs(patternToPaint)
