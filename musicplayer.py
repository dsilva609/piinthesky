import pygame;

def PlayBall():
	pygame.mixer.init();
	pygame.mixer.music.load("/home/pi/Downloads/baseball.mp3")
	pygame.mixer.music.play()

	while pygame.mixer.music.get_busy() == True:
		continue

# PlayBall();
# PlayBall();

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7,0)

try:
	while True:
		if (GPIO.input(11) == 1):
			GPIO.output(7,1)
			PlayBall();
		else:
			GPIO.output(7,0)
except KeyboardInterrupt:
	GPIO.cleanup()