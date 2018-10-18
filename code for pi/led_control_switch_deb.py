#!/usr/bin/env python
import time 
import RPi.GPIO as GPIO

#set input and output gpio physical pin numbers 
switch = 12 
led = 11

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup(switch,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,GPIO.LOW)

while True:
   if GPIO.input(switch) == 1 :
      time.sleep(0.25)  # debounce
      start_time = time.time()
      GPIO.output(led,GPIO.LOW)
      while GPIO.input(switch) == 1 :
         if time.time() - start_time > 2.75:
            GPIO.output(led,GPIO.HIGH)
   else:
    import RPi.GPIO as GPIO  
