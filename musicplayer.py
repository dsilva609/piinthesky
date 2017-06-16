import pygame
import RPi.GPIO as GPIO
import random
import time


directory = "/home/pi/Downloads/"
song = "carelesswhisper.mp3"
sensorPin = 11
ledPin = 7
timeoutMinSec = 30
timeoutMaxSec = 60

def SetUp():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, 0)

	pygame.mixer.init();
	pygame.mixer.music.load(directory + song)
	
def HitIt():
	pygame.mixer.music.play()

	while pygame.mixer.music.get_busy() == True:
		continue
		
def WaitInHiding():
	while True:
		if (GPIO.input(sensorPin) == 0):
			GPIO.output(ledPin, 1)
			HitIt()
			time.sleep(random.randint(timeoutMinSec, timeoutMaxSec))
		else:
			GPIO.output(ledPin, 0)

if __name__ == "__main__":
	try:
		SetUp()
		WaitInHiding()
	except KeyboardInterrupt:
		GPIO.cleanup()
