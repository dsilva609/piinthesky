import sys
import pygame
import RPi.GPIO as GPIO
import random
import time
import Adafruit_CharLCD as LCD
import sqlite3

goRandom = False

song = "carelesswhisper.mp3"
songs = [] #['carelesswhisper.mp3', 'childrenofthecorn.mp3', 'manonthesilvermountain.mp3', 'ringaroundtherosie.mp3', 'kungfufighting.mp3', 'spongebob.mp3', 'pokerface.mp3']
sensorPin = 17
ledPin = 4

timeoutMinSec = 30
timeoutMaxSec = 60

#lcd gpio pins
rs = 26
en = 19
d4 = 13
d5 = 6
d6 = 5
d7 = 20
cols = 16
lines = 2
lcd = LCD.Adafruit_CharLCD(rs,en,d4,d5,d6,d7,cols,lines)

conn = sqlite3.connect('song.db')
c = conn.cursor()

def SetUp():
	GPIO.setwarnings(0)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sensorPin, GPIO.IN)#, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, 0)

	pygame.mixer.init();
	
	CreateDatabase()
	LoadSongs()

	for x in range(5,0, -1):
		lcd.clear()
		lcd.message("Arming bomb:" + str(x))
		time.sleep(x)
		print x


	lcd.clear()
	lcd.message("sayonara")
	time.sleep(2)
	
	lcd.clear()
	lcd.message("Gotcha.\nSystem Active")
	time.sleep(2)
	lcd.clear()

def CreateDatabase():
		c.execute('CREATE TABLE IF NOT EXISTS song(name TEXT)')
	
def LoadSongs():
	c.execute('SELECT * FROM song')
	songs = c.fetchall()
	
	for song in songs
		print song
	
	c.close()
	conn.close()
	
def HitIt():
	if goRandom:
		songIndex = random.randint(0, len(songs) - 1)
		songToPlay =  songs[songIndex]
	else: songToPlay = song

	lcd.clear()
	lcd.message("Now playing:\n" + songToPlay)

	pygame.mixer.music.load(songToPlay)
	pygame.mixer.music.play()

	while pygame.mixer.music.get_busy() == True:
		continue
		
def WaitInHiding():
	while True:
		if (GPIO.input(sensorPin) == 1):
			GPIO.output(ledPin, 1)
			HitIt()
			
			#time.sleep(random.randint(timeoutMinSec, timeoutMaxSec))
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