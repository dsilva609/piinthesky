import sys
import pygame
import RPi.GPIO as GPIO
import random
import time

goRandom = False
song = "carelesswhisper.mp3"
songs = ['carelesswhisper.mp3', 'childrenofthecorn.mp3', 'manonthesilvermountain.mp3', 'ringaroundtherosie.mp3', 'kungfufighting.mp3', 'spongebob.mp3', 'pokerface.mp3']
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

def HitIt():
	if goRandom:
		songIndex = random.randint(0, len(songs) - 1)
		songToPlay =  songs[songIndex]
	else: songToPlay = song

	#print "playing: " + songToPlay
	pygame.mixer.music.load(songToPlay)
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
	if sys.argv[1:]:
		goRandom = True
	try:
		SetUp()
		WaitInHiding()
	except KeyboardInterrupt:
		GPIO.cleanup()
