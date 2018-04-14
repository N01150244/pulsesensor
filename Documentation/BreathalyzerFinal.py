import pyrebase
import time
import serial
import RPi.GPIO as GPIO
#GPIO.setup(11,GPIO.OUT)
#GPIO.VERSION
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
 
from smbus import SMBus 
bus = SMBus(1)

def read_ain(i):    
    global bus
    #bus.write_byte_data(0x48, 0x40 | ((i) & 0x03), 0)
    bus.write_byte(0x48, i)
    bus.read_byte(0x48)#first 2 are last state, and last state repeated.
    bus.read_byte(0x48)   
    return bus.read_byte(0x48)

config = {
    "apiKey": "AIzaSyBMu4FC-4kiSRXdmLOQgFZOUMG15JBHG-Y",
    "authDomain": "breathalyzer.firebaseapp.com",
    "databaseURL": "https://breathalyzer.firebaseio.com",
    "projectId": "breathalyzer",
    "storageBucket": "breathalyzer.appspot.com",
    "messagingSenderId": "179506469389"
  }

firebase = pyrebase.initialize_app(config)


applicant = input("Enter your username:")
     
i = 0
count = 0
j = 0
while(i<5):
    heartrate1 = read_ain(1)
    alcohol = read_ain(2)*0.001
    read_ser=ser.readline()
    hr2 = read_ser.decode('utf-8')
    print ("\n----Testing----\n")
    print("HeartRate Sensor: {0:.0f} BPM".format(heartrate1))
    print ("Alcohol Reading: {0:.2f}%\n".format(alcohol))
    print ("Wireless Heart Rate : %s\n" %hr2)
    time.sleep(3)
    i+=1
    
   
db = firebase.database()
result = db.child("user").child(applicant).update({'Heart Rate1':heartrate1})
result2 = db.child("user").child(applicant).update({'Alcohol Reading':alcohol})
result3 = db.child("user").child(applicant).update({'Heart Rate2':hr2})
result4 = db.child("user").child(applicant).child("Past Results HR1").push(heartrate1)
result5 = db.child("user").child(applicant).child("Past Results Alcohol Reading").push(alcohol)
result6 = db.child("user").child(applicant).child("Past Results HR2").push(hr2)
    
