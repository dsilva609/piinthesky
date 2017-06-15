import pygame;

def PlayBall():
	pygame.mixer.init();
	pygame.mixer.music.load("/home/pi/Downloads/baseball.mp3")
	pygame.mixer.music.play()

	while pygame.mixer.music.get_busy() == True:
		continue

PlayBall();
PlayBall();
