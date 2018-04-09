from firebase import firebase
firebase = firebase.FirebaseApplication('https://breathalyzer.firebaseio.com/')
import time
import serial
import RPi.GPIO as GPIO
GPIO.VERSION
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.IN)
ser=serial.Serial("/dev/ttyACM1", 9600)
ser.baudrate=9600
def blink(pin):

      GPIO.output(pin,GPIO.HIGH)
      time.sleep(1)
      GPIO.output(pin, LOW)
      time.sleep(1)
      return

#GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
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
      
i = 0
count = 0
j = 0
while(i<5):
    heartrate1 = read_ain(1)
    alcohol = read_ain(2)*0.001
    read_ser=ser.readline()
    
    print "\n----Testing----\n"
    print("HeartRate Sensor: {0:.0f} BPM".format(heartrate1))
    print ("Alcohol Reading: {0:.2f}%\n".format(alcohol))
    print ("Wireless Heart Rate : %s\n" %read_ser)
    time.sleep(3)
    i+=1
    #heartrate2 = int(read_ser)
   
   
result = firebase.patch('https://breathalyzer.firebaseio.com/user/'+applicant,{'Heart Rate1':heartrate1}) 
result2 = firebase.patch('https://breathalyzer.firebaseio.com/user/'+applicant,{'Alcohol Reading':alcohol})
result3 = firebase.patch('https://breathalyzer.firebaseio.com/user/'+applicant,{'Heart Rate2':read_ser})     

