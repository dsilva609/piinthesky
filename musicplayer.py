import pygame;
import RPi.GPIO as GPIO

song = "carelesswhisper"

def SetUp():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(7, GPIO.OUT)
	GPIO.output(7,0)

	pygame.mixer.init();
	pygame.mixer.music.load("/home/pi/Downloads/" %s ".mp3")
	
def HitIt():
		pygame.mixer.music.play()

	while pygame.mixer.music.get_busy() == True:
		continue
		
def WaitInHiding():
	while True:
		if (GPIO.input(11) == 0):
			GPIO.output(7,1)
			HitIt()
		else:
			GPIO.output(7,0)

if __name__ == "__main__":
	try:
		WaitInHiding()
	except KeyboardInterrupt:
		GPIO.cleanup()