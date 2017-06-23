from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD(rs=12,en=16,d4=29,d5=31,d6=33,d7=35,cols=16,lines=2)

lcd.clear()
print "test"
lcd.message('HeavyMetal\n Friday')
print "done"
sleep(10)