#import GPIO and time library
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

ledPin = 22

#setup the ledpin(i.e. GPIO22) as output
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)

try:
    while True:
        GPIO.output(ledPin, True)
        print("LED ON")
        sleep(1)
        GPIO.output(ledPin, False)
        print("LED OFF")
        sleep(1)

finally:
    #reset the GPIO Pins
    GPIO.output(ledPin, False)
    GPIO.cleanup()

# end of code
