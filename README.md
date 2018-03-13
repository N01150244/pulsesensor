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
This page is created to help you to create your own Hearrate sensor project. In order to fix the problem of drinking and driving, we (Maheshwerie Samaroo, Mohita Prabhakar and Karandeep Singh) chose the Heart Rate Educational Starter Kit, Alcohol Gas sensor and Pulse sensor respectively. Instead of people thinking they're okay to drive with alcohol in their body, they can use our project to see if there is a large amount of alcohol in their body along with seeing their heart rate. It's a cheap alternative, and isn't too hard to make yourself.
<br>
Using a gas and two heartbeat sensors, users can plug those into a PCB and use a raspberry pi to display the readings on either a computer or phone on our mobile application.

![Plan](https://github.com/N01150244/pulsesensor/blob/master/Plan.png)

### Bill of Materials
Given below are parts and material required for this project. Most of these
parts are pretty cheap which makes this project not too expensive, but that is
because we already had our respective raspberry pis, electronic parts kit, and  PCB kits which were
paid for as a part of our tuition. 

| **Item**                               | **Quantity** | **Cost**  | **Supplier & Part Number**                  |
|--------------------------------------- |--------------|-----------|---------------------------------------------|
| Raspberry Pi 3 Starter Kit             | 1            | \$79.99   | (Canakit) Amazon - B01CCF9BYG               |
| XD-58C Sensor                          | 1            | \$18.99   | (JutaTech) Amazon.ca - B01AUVMFIS           |
| MQ3 Alcohol/Gas Sensor                 | 1            | \$8.80    | (Creatron) creatroninc.com - SPEDE-000030.  |
| Heart Rate Educational Starter Pack    | 1            | \$65.00   | (AdaFruit) adafruit.com - 1077              |
| Electronics Parts Kit                  | 1            | \$119.99  | Humber - SKU \#163                          |
| Jumper Wires (120 pack)                | 1            | \$19.99   | (Elegoo) Amazon.ca - B01EV70C78             |
| Solder Kit                             | 1            | \~\$40.00 | Humber                                      |
| Soldering Iron                         | 1            | \~\$20.00 | Humber                                      |
| Power Cables/Connectors                | 1            | included  | Humber/Amazon                               |

Again, these are just the parts and prices for the things we bought. Prices may
change over time, but our total comes to around \$360.

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
To keep things simple, for mechanical assembly, everything will be broken into sections. First, there will be a description on how to setup your raspberry pi, what is needed to be done in order for it to work properly. Next, steps to create your own PCB will be detailed. After that, steps to connect and power up will be detailed.

### Raspberry Pi Setup
Once you’ve acquired your Raspberry Pi, the first thing to do would be to get a keyboard and a mouse connected. Please note that whenever connecting any new device or making any new connections to the Raspberry Pi, please ensure that you Pi is powered off completely. For the Pi that was used for this project, what was noticed, was that when connections were made while the pi was powered on, the pi would freeze and become unresponsive. The next thing to do would be to insert the SD card which comes with the Pi. There’s many ways in which to connect the Pi to a display but in this case, a HDMI cable was used to connect to a monitor. The final thing would be to plug the Pi in. A black screen will be displayed at first, which is fine and absolutely normal. You will need to run an update which can be done by issuing the “sudo apt-get update” command. Please note that your Raspberry Pi must have an active internet connection in order for this to work. You can purchase a wifi dongle separately for this or use a LAN cable. In this case, we had neither so using one of our mobile phones, we used a feature called “Mobile Tethering” which enables the phone to share its internet connection when it is connected via USB. The final step would be to download the python code needed for this project which can be found on the Github. 

-  [Python code for sensors](https://github.com/N01150244/pulsesensor/blob/master/Breathalyzer.py)

### PCB Soldering
The next thing to start working on would be the PCB (Printed Circuit Board). The PCB which was provided  by the Humber Prototype Lab is what was used to facilitate majority of the project. First you need to download the software EAGLE and then open the appropriate files. The schematic and board files were provided to us by our professor. 
Assistance was given to us when needed by Kelly and Vlad who both work at the Prototype Lab. They were more than willing to assist whenever students needed it. Most of the soldering was done by looking at a reference model. Tools were provided by the lab, free of cost for the soldering of the PCB.


-  [Schematic File](https://github.com/N01150244/pulsesensor/blob/master/HSHV4-student%20version.sch)<br>
-  [Board File](https://github.com/N01150244/pulsesensor/blob/master/HSHV4-student%20version.brd)<br>


 Here’s what your PCB should look like when you’ve finished.
![PCB](https://github.com/N01150244/pulsesensor/blob/master/pcb1.jpg)

### Assembling the Project
Once the Raspberry Pi is properly set-up, and your PCB is finished soldering, the rest of the project can now be assembled. The PCB needs to be “plugged in” directly to the raspberry pi. In this case, we plugged the PCB into the Raspberry Pi and then connected a pi cobbler plus breakout cable which we then connected to a breadboard. This makes it easier for you to make your connections. Note that it isn’t a requirement for you to buy the pi cobbler and breakout cable. The PCB must be connected to the header which is labelled “PFC-ADC”. Please remember that the Raspberry Pi must be completely powered off. The first sensor which we will speak about will be the XD-58C sensor (pulse rate sensor). The XD-58C sensor has three cables, which are colored purple, red and black. The red and black cables must be connected to 3.3V and GND  respectively using the DTC header on the PCB. The purple cable must be connected to the AIN1 pin on the PCB. Please make sure that the Raspberry Pi is powered off completely before making these connections or else you will be at a risk of shorting a connection on the board. The second set of sensors which were used were the Polar T34 Heart Rate Transmitter and the Polar Heart Rate Receiver. Connecting the Heart Rate Receiver is simple. The third and final sensor which was used was the MQ3 Alcohol/Gas Sensor. The Raspberry pi is connected with the Mq3 sensor in such a way that VCC, D out and A out of the MQ3 Sensor is connected to the pin Vcc(4),Ground(6) and GPIO14(8) respectively as given below in the picture. 

### Power Up
Once all the connections have been made, the last thing left to do would be to plug the Raspberry Pi in. A quick check can be done to ensure that the sensors are in proper working order. The command “i2cdetect -y 1” can be issued in the terminal and 48 will be returned. The next step will be to run the code previously downloaded from the Github. First you must navigate to the location of the code via the Terminal and then issue the command “python Breathalyzer.py”. If the sensors are correctly connected, then the code should work perfectly.

### Unit Testing
For unit testing, we individually tested each sensor with individual pieces of code before combining into one piece of code. For the XD-58C sensor, the sensor should detect a heartbeat and it’s reading should be shown on the terminal screen. The same conditions are applicable to the other two sensors.

### Production Testing
This is the final step. At this stage everything should be in perfect working order. We’ve tested our code and sensors based on our Firebase Database. Basically if everything is in working order, then results from the sensors should be posted to our real time Firebase database. Also, this project works hand in hand with a mobile application which can be downloaded from the Google Play Store. Below is a simple diagram for you to understand the process flow of our project. The WebPage is a current work in progress and will be updated on our Github.

### Reproducible??
If this guide is followed step by step, then you shouldn’t have any issues with the set-up. As long as you have your parts and components, this project can be completed within a week. The best advice especially if you’re trying to meet a deadline, is to get started as soon as you receive your parts and be sure to track and slot your time wisely.<br>
![Mysensor](https://github.com/N01150244/pulsesensor/blob/master/Sensors(combined).JPG)

