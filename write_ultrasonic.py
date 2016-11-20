#Trigger 31
#Echo 32
import RPi.GPIO as GPIO
import time
import os

f=open("/home/pi/Documents/temp_range.txt","w")

TRIG = 31
ECHO = 32

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	
	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
	while True:
		dis = distance()
#		print dis, 'cm'
#		print ''
		f.write("%0.2f\n" % dis)
                f.flush()
                os.fsync(f)
		time.sleep(2)

def destroy():
	GPIO.cleanup()
	f.close()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
