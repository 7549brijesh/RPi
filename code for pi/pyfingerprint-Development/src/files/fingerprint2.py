import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio


enrol=5
delet=6
led=26

HIGH=1
LOW=0

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(enrol, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(delet, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(led, gpio.OUT)

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)

print('Currently used finger templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))


def enrollFinger():
    print('Waiting for finger...')
    while ( f.readImage() == False ):
        pass
    f.convertImage(0x01)
    result = f.searchTemplate()
    positionNumber = result[0]
    if ( positionNumber >= 0 ):
        print('Finger already exists at position #' + str(positionNumber))
        time.sleep(2)
        return
    print('Remove finger...')
    time.sleep(2)

    print('Waiting for same finger again...')
    while ( f.readImage() == False ):
        pass
    f.convertImage(0x02)
    if ( f.compareCharacteristics() == 0 ):
        print ("Fingers do not match")
        time.sleep(2)
        return
    f.createTemplate()
    positionNumber = f.storeTemplate()
    print('Finger enrolled successfully!')
    
    print('New template position #' + str(positionNumber))
    time.sleep(2)

def searchFinger():
    try:
        print('Waiting for finger...')
        while( f.readImage() == False ):
            #pass
            time.sleep(.5)
            return
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1 :
            print('No match found!')
            time.sleep(2)
            return
        else:
            print('Found finger at position #' + str(positionNumber))
            time.sleep(2)

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
    
def deleteFinger():
    positionNumber = 0
    count=0
    while gpio.input(delet) == True:   # here delet key means ok
      positionNumber = input('Please enter the template position you want to delete: ')
      positionNumber = int(positionNumber)
      if f.deleteTemplate(positionNumber) == True :
        print('Template deleted!')
        time.sleep(1)
        print('Currently used finger templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
        time.sleep(1)
        return
      

print ("Fingerprint Enroll Program ")
time.sleep(3)
flag=0


while 1:
    gpio.output(led, HIGH)
    
    if gpio.input(enrol) == 0:
        gpio.output(led, LOW)
        enrollFinger()
    elif gpio.input(delet) == 0:
        gpio.output(led, LOW)
        while gpio.input(delet) == 0:
            time.sleep(0.1)
        deleteFinger()
    else:
        searchFinger()  









    
