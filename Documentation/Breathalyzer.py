from firebase import firebase
firebase = firebase.FirebaseApplication('https://breathalyzer.firebaseio.com/')
import time
import RPi.GPIO as GPIO
GPIO.VERSION
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(8,GPIO.IN)
GPIO.setwarnings(False)
from smbus import SMBus

bus = SMBus(1)

def read_ain(i):    
    global bus
    #bus.write_byte_data(0x48, 0x40 | ((i) & 0x03), 0)
    bus.write_byte(0x48, i)
    bus.read_byte(0x48)#first 2 are last state, and last state repeated.
    bus.read_byte(0x48)
    return bus.read_byte(0x48)

applicant = raw_input("Enter your username:")
#while(1):
#heartrate = 101
#heartrate = read_ain(1)
input = GPIO.input(8)


if input == 0:
	print "Alcohol is detected"
        print (input)
	result2 = firebase.patch('https://breathalyzer.firebaseio.com/user/'+applicant,{'Alcohol Reading':input})

else:
        print "Testing -----------"
        print ("Alcohol not Detected")
	result2 = firebase.patch('https://breathalyzer.firebaseio.com/user/'+applicant,{'Alcohol Reading':input})
	#j+=1
	#time.sleep(2)

i = 0
while(i<3):
	heartrate = read_ain(1)
	print "Testing HeartRate-------------\n"
	if(heartrate<60) or (heartrate>100):
		GPIO.output(11,0)
		GPIO.output(12,1)
	else:
	
		GPIO.output(11,1)
		GPIO.output(12,0)
    		#print("Heart Rate Sensor: {0:.0f} BPM\n".format(heartrate))
	i+=1
    	time.sleep(2)
print("Heart Rate Sensor: {0:.0f} BPM\n".format(heartrate))
result = firebase.patch('https://breathalyzer.firebaseio.com/user/'+applicant,{'Heart Rate1':heartrate})


#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8,GPIO.IN)

#while 1:
#input = GPIO.input(8)
#if input == 0:
#        print "Alcohol is detected"
#        print (input)
#else:
#        print "Alcohol is not detected"
#        print (input)



