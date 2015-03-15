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
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	right_button = GPIO.input(26)
	left_button = GPIO.input(20)
	up_button = GPIO.input(13)
	down_button = GPIO.input(16)
	a_button = GPIO.input(6)
	b_button = GPIO.input(21)
	select_button = GPIO.input(5)
	start_button = GPIO.input(19)

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
	if a_button == False:
		print "A"
		patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
       		                  [ 0, 0, 1, 1, 1, 1, 0, 0 ],
                       		  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
                                  [ 0, 1, 1, 1, 1, 1, 1, 0 ],
                                  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
                                  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
                                  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                ]

	if b_button == False:
		print "B"
		patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
       		                  [ 0, 1, 1, 1, 1, 1, 0, 0 ],
                       		  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
                                  [ 0, 1, 1, 1, 1, 1, 0, 0 ],
                                  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
                                  [ 0, 1, 0, 0, 0, 0, 1, 0 ],
                                  [ 0, 1, 1, 1, 1, 1, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                ]
	if select_button == False:
		print "SELECT"
		patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
       		                  [ 0, 1, 1, 0, 1, 1, 1, 0 ],
                       		  [ 1, 0, 0, 0, 1, 0, 0, 0 ],
                                  [ 0, 1, 0, 0, 1, 1, 1, 0 ],
                                  [ 0, 0, 1, 0, 1, 0, 0, 0 ],
                                  [ 0, 0, 1, 0, 1, 0, 0, 0 ],
                                  [ 1, 1, 0, 0, 1, 1, 1, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                ]
	if start_button == False:
		print "START"
		patternToPaint = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
       		                  [ 0, 1, 1, 0, 1, 1, 1, 0 ],
                       		  [ 1, 0, 0, 0, 0, 1, 0, 0 ],
                                  [ 0, 1, 0, 0, 0, 1, 0, 0 ],
                                  [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                                  [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                                  [ 1, 1, 0, 0, 0, 1, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                                ]

	paintLEDs(patternToPaint)
#	time.sleep(0.2)
