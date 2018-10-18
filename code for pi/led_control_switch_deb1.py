import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
switch = 12 
led = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)     # set up BOARD GPIO numbering  
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set GPIO pin 12 as input (button)  
GPIO.setup(led, GPIO.OUT)   # set GPIO24 as an output (LED)  
  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(switch): # if switch == 1  
            print ("Switch is press" ) 
            GPIO.output(led, 1)         # set port/pin value to 1/HIGH/True  
        else:  
            GPIO.output(led, 0)         # set port/pin value to 0/LOW/False  
        sleep(0.2)         # wait 0.2 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
