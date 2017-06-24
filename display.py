from time import sleep
import Adafruit_CharLCD as LCD

rs = 26
en = 19
d4 = 13
d5 = 6
d6 = 5
d7 = 20
cols = 16
lines = 2


lcd = LCD.Adafruit_CharLCD(rs,en,d4,d5,d6,d7,cols,lines)

lcd.clear()

lcd.message('man on the\n silver mountain')





sleep(3)