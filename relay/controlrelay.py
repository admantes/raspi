#!/usr/bin/python
#import RPi.GPIO as GPIO
import time
import sys
 
#GPIO.setmode(GPIO.BCM)

# init list with pin numbers
pinList = [2, 3, 4, 17]
#for i in pinList: 
	#print(i)
    #GPIO.setup(i, GPIO.OUT) 
    
	
total = len(sys.argv)
 
# Get the arguments list 
cmdargs = sys.argv
val = cmdargs[1]

pin = val[0:1]
mode = val[1:2]

#time.sleep(1)
curPin = 0

if pin == "9":
	print ("ALL MODE")
else:
	curPin = pinList[int(pin)]	

#GPIO.setup(curPin, GPIO.OUT) 

#if mode == 1:
	#GPIO.output(curPin, GPIO.HIGH)
#else:
	#GPIO.output(curPin, GPIO.LOW)
	
	

# Print it
#print ("The total numbers of args passed to the script: %d " % total)
print (curPin)
print ("VALUES ARE: %s %s " % (pin,mode) )

# find more information on this script at
# http://youtu.be/WpM1aq4B8-A