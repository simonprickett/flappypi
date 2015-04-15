import RPi.GPIO as GPIO
import time

def myCallback(channel):
	print "A pressed (GPIO " + str(channel) + ")"

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.FALLING, callback=myCallback, bouncetime=200)

while(True):
	time.sleep(1)
