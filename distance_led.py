#Import libraries

import RPi.GPIO as GPIO
import time

#For GPIO numbering, choose BCM (Broadcom GPIO numbers) 
GPIO.setmode(GPIO.BCM)

#Disables warnings GPIO.cleanup not needed.
GPIO.setwarnings(False) 

#ports for sonar sensor
TRIG = 23
ECHO = 24

#Prepares GPIO ports.
# 21 = RED LED
# 16 = GREEN LED 
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

print ("Distance Measurement In Progress")

try:
    #prepares sonar sensor
    while True:
        GPIO.output(TRIG, False)
        print ("Waiting For Sensor To Settle")
        time.sleep(2)
    
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()
          
        #Math for converting pulse duration to distance in CM 
        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        print ("Distance:",distance,"cm")
        
        #if distance is smaller or equal then 150 turn on RED LED 
        if distance <= 149:
            GPIO.output(21, GPIO.HIGH)
            print("Rode led aan!")
        #else turn RED LED off
        else:
            GPIO.output(21, GPIO.LOW)
            print("Rode led uit!")
        #if distance is bigger or equal then 150 turn on GREEN LED 
        if distance >= 150:
            GPIO.output(16, GPIO.HIGH)
            print("Groene led aan!")
        else:
            #else turn GREEN LED off
            GPIO.output(16, GPIO.LOW)
            print("Groene led uit!")

        
# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
except KeyboardInterrupt:
    print("Cleaning up!")
    gpio.cleanup()
    
#Whenever an error occurs it will be printed out. 
except Exception as e:
    print("Error has occurred", e)