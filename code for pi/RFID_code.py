import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BOARD)
greenLED = 37
redLED = 35
buzzer = 33

GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

GPIO.setup(greenLED, False)
GPIO.setup(redLED, False)

GPIO.output(buzzer, True)
time.sleep(0.1)
GPIO.output(buzzer, False)
time.sleep(0.1)
GPIO.output(buzzer, True)
time.sleep(0.1)
GPIO.output(buzzer, False)
time.sleep(0.1)

def read_rfid ():
    ser = serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 9600
    data = ser.read(12)
    ser.close()
    return data

try:
    
    while True:
     id = read_rfid ()
     print (id)

     if id=="400037052656":
         print("Access Granted")
         GPIO.output(greenLED, True)
         GPIO.output(redLED, False)
         GPIO.output(buzzer, False)
         time.sleep(2)
     else:
         print("Access Denied")
         GPIO.output(greenLED, False)
         GPIO.output(redLED, True)
         GPIO.output(buzzer, True)
         time.sleep(2)
         GPIO.output(greenLED, False)
         GPIO.output(redLED, False)
         GPIO.output(buzzer, False)
finally:
    GPIO.cleanup()
            
