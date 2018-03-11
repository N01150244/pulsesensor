import RPi.GPIO as io # import the GPIO library we just installed but call it "r we just installed but call it "Streamer"
import time
SAMPLE_COUNT = 10
## name the bucket and individual access_key
## the bucket_key will send all of our messages to the same place
## the access_key tells Initial State to send the messages to you
##streamer=Streamer(bucket_name="Heart Rate Monitor",bucket_key="heartrate",access_key="t5A3BI7v9R8iARMwh0fgjzh7sG9E9JJr")
 
## set GPIO mode to BCM
## this takes GPIO number instead of pin number
io.setmode(io.BCM)
io.setwarnings(False)
 
receiver_in = 23 # this is the GPIO number our receiver is connected to
LED_in = 18 # GPIO number the LED is connected to
 
io.setup(receiver_in, io.IN) # initialize receiver GPIO to take input
io.setup(LED_in, io.OUT) # initialized LED GPIO to give output
 
io.output(LED_in, io.LOW) # start with LED off
 
## log that everything is ready to receive the heartbeat signal
print "Waiting for Beat"
 
## this try block looks for 1 values (indicate a beat) from the transmitter
try:
    firstBeatTime = time.time()
    sampleCounter = 0
    Count = 10
    while Count <= 10:
        Count +1
        
        sample = io.input(receiver_in)

        if sample == 1:
            io.output(LED_in, io.HIGH)
            print "beat detected"
            # turn LED on
          ##  sampleCounter = sampleCounter + 1
            #if sampleCounter == SAMPLE_COUNT:
             #   sampleCounter = 0 # reset the sample counter

                # calculate beats per minute given the SAMPLE_COUNT
              #  sampleMinutes = (time.time() - firstBeatTime)/60
               # bpm = sampleMinutes * SAMPLE_COUNT

                # stream
            
        else:
            io.output(LED_in, io.LOW) # turn LED off
 
        # Set the previous sample to the current sample so that it can be used to
        # evaluate if at the front edge of the heartbeat and not count it more than
        # once if already in the high position
        previousSample = sample
## this allows you to end the script with ctrl+c
except KeyboardInterrupt:
    print "Interrupt"
    io.cleanup()
