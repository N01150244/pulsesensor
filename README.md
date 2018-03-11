 # Build Instructions for Breathalyzer:Heartrate Sensor

## Table of Contents
1. [Introduction](#introduction)
2. [Bill of Materials](#bill-of-materials)
3. [Time Commitment](#time-commitment)
4. [Mechanical Assembly](#mechanical-assembly)
5. [PCB Soldering](#pcb-soldering)
6. [Power Up](#power-up)
7. [Unit Testing](#unit-testing)
8. [Production Testing](#production-testing)
9. [Reproducible](#reproducible)

### Introduction
This page is created to help you to create your own Hearrate sensor project. In orderto fix the problem of drinking and driving, my partners (Maheshwerie Samaroo), (Mohita Prabhakar) and I (Karandeep Singh) chose Heart Rate Educational Starter Kit, Alcohol Gas sensor and Pulse sensor respectively.Instead of people thinking they're okay to drive with alcohol in their body, they can use our projectto see if there is a large amount of alcohol in their body along with seeing their heart rate. It's a cheap alternative, and isn't too hard to make yourself.
<br>
Using a gas and two heartbeat sensors, users can plug those into a PCB and use a raspberry pi to display the readings on either a computer or phone on our mobile application.

![Plan](https://github.com/N01150244/pulsesensor/blob/master/Plan.PNG)

### Bill of Materials
Given below are parts and material required for this project. Most of these
parts are pretty cheap which makes this project not too expensive, but that is
because we already had our respective raspberry pis, electronic parts kit, and  PCB kits which were
paid for as a part of our tuition. 

| **Item**                   | **Quantity** | **Cost**  | **Supplier & Part Number**        |
|----------------------------|--------------|-----------|-----------------------------------|
| Raspberry Pi 3 Starter Kit | 1            | \$79.99   | (Canakit) Amazon - B01CCF9BYG     |
| XD-58C Sensor              | 1            | \$18.99   | (JutaTech) Amazon.ca - B01AUVMFIS |
| Electronics Parts Kit      | 1            | \$119.99  | Humber - SKU \#163                |
| Jumper Wires (120 pack)    | 1            | \$19.99   | (Elegoo) Amazon.ca - B01EV70C78   |
| Solder Kit                 | 1            | \~\$40.00 | Humber                            |
| Soldering Iron             | 1            | \~\$20.00 | Humber                            |
| Power Cables/Connectors    | 1            | included  | Humber/Amazon                     |

Again, these are just the parts and prices for the things we bought. Prices may
change over time, but our total comes to around \$300.

### Time Commitment
If you work on this continuously with no other
tasks in your way, it shouldn't take that long considering you do everything
correctly! In this chart below, we break down how much time was taken on each
main task of the project.

| ThingS you need to do                       | Time Taken To Complete (Approx.) |
|---------------------------------------------|----------------------------------|
| Looking for and Purchasing Parts + Delivery | 1.5 hours + 1 week               |
| Assembling case and setting up Raspberry Pi | 1 hour                           |
| Editing your custom PCB                     | 30 minutes                       |
| Soldering/Testing/Troubleshooting your PCB  | 3.5 hours                        |
| Creating a case for your project            | 1 hour                           |
| Testing/calibrating the sensors             | 2 hours                          |
| Setting up the project                      | 10 minutes                       |

After breaking down the parts of the project, it is pretty easy to tell that
it's not a very time consuming project to complete. If you are very committed to
this project then it shouldn't be very difficult to complete this in these time
frames.

### Mechanical Assembly
To keep things simple, for mechanical assembly I'm going to break up the parts into main sections. First I'll talk about how you have to set up the raspberry Pi, what needed to be done in order for it to work properly. Next I'll talk about creating your own PCB, and soldering it. After that I will talk about connecting the parts together and powering it up.
### Raspberry Pi Setup
Once you receive your Raspberry Pi, you can start by connecting a keyboard and mouse to the USB ports. Next go ahead and push in the SD card included, and use the HDMI connector and connect it to a monitor so you will be able to see the display. Lastly, plug in the power adapter to turn on the raspberry pi. Things will flash on the screen and text will flood a black terminal, but eventually it will stop, allowing for input. The most important thing to do is run the command "sudo apt-get update" which is really important because it will give the newest and most stable updates for your raspberry pi. 
Connect to the internet in whichever way is best, and download the python file I created and put it in an easy place to find (found below). Locate it in a terminal and compile it using "python pulse.py".

-  [Python code for sensor](https://github.com/N01150244/pulsesensor/blob/master/pulse.py)

### PCB Soldering
Next thing to start working on would be the PCB. The PCB provided to me by the Humber Prototype Lab is what I used to hold majority of my project. First download the program EAGLE, and the required board and schematic file which is provided below. The schematic and board file are just a generic student file so the name will need to be changed. Lastly I went to the prototype lab and asked what else they needed for me to print my board, and they asked for these two files and the rest was done by them.

-  [Schematic File](https://github.com/N01150244/pulsesensor/blob/master/HSHV4-student%20version.sch)<br>
-  [Board File](https://github.com/N01150244/pulsesensor/blob/master/HSHV4-student%20version.brd)<br>

When soldering the PCB, Kelly at the Prototype Lab really helped out. If you had a question on how to test it or where to solder some things, they would help you out. Majority of the soldering was done while looking at the reference model they had at the lab, I also used the solder and soldering iron they had there so I didn't need to buy my own. Once done, you should consult to Vlad and Kelly to make sure you've done it right, they will show you how to properly test it to make sure it works. Below is just a visual of what my PCB looked like when it was completed.

![PCB](https://github.com/N01150244/pulsesensor/blob/master/pcb1.jpg)

### Assembling the Project
When the Raspberry Pi is setup, and the PCB is finished and soldered you can now set up the rest of the project. Get the Modular Sense Hat and connect it properly into the header labelled PFC-ADC on the board. Take the Heartbeat sensor, connect positive to VCC in the header labelled DS-RTC on the board, negative to ground, and signal ping to the AIN2 pin on the Modular Sense Hat. Lastly, using the 24-pin GPIO header on the PCB board, connect it to the Raspberry Pi firmly so it's set (MAKE SURE THE PI IS OFF). Now we can move to the power up.

### Power Up
Once everything above was completed, the only thing left is power up. Do a quick check and make sure everything is wired correctly, and make sure that there are no problems. Go ahead and plug the USB's into the Raspberry Pi, power it on and see if it works. You can see if the sensors are being detected by using the command "i2cdetect -y 1" on a terminal and you should see 48, which corresponds to the Modular Sense Hat! This is the big and final step, if everything is working correctly, the code should work without any problems. So go look for the code that you previously downloaded, compile it and run it using "python PULSE.py".

### Unit Testing
For unit testng there wasn't a lot of things to be done. For the heartbeat sensor all you need to do is compile it, run it and now put a finger onto the green light and watch the screen. If done correctly the reading should drop down to a number lower than 10, and then give you a more accurate reading of something between 70-80 after five or so seconds. If both of these work properly, you're good to go to the final step.

### Production Testing
Now that we're at the last step and we're sure that everything is working properly, run it. If everything works properly the code should work and you should be getting successful readings from the sensor if working properly. Also code for the LED on the PCB board is included so now, the LED will be red if a impossible reading for the heart beat is detected, so if the reading is less than 60 or greater than 100, the reading is inaccurate or your heart rate is not stable.

### Reproducible??
If you follow this guide step by step and everything seems to be working at the end... then yes, this project is very reproducible! In a few days, you can have your very own product, the only thing that would keep you from doing it much faster would be the delivery dates on items. After putting in the hard work, you can use it to impress people with and hopefully use it yourself to keep you far away from drunk driving! You yourself can help reduce the problem of drinking and driving just by making this, so get started.<br>
![Mysensor](https://github.com/N01150244/pulsesensor/blob/master/mysensor.jpg)
![Mysensor2](https://github.com/N01150244/pulsesensor/blob/master/mysensor2.JPG)
