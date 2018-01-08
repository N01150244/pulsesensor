import time
import RPi.GPIO as GPIO
GPIO.VERSION
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

from smbus import SMBus

bus = SMBus(1)

def read_ain(i):    
    global bus
    #bus.write_byte_data(0x48, 0x40 | ((i) & 0x03), 0)
    bus.write_byte(0x48, i)
    bus.read_byte(0x48)#first 2 are last state, and last state repeated.
    bus.read_byte(0x48)
    return bus.read_byte(0x48)

while(True):
    heartrate = read_ain(1)

    print "-------------------------\n"
    if(heartrate<60) or (heartrate>100):
	GPIO.output(11,0)
	GPIO.output(12,1)
    else:
	GPIO.output(11,1)
	GPIO.output(12,0)
    print("Heart Rate Sensor: {0:.0f} BPM\n".format(heartrate))
    time.sleep(1)#sec