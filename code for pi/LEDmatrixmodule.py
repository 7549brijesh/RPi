#Program to Display message on LED matrix module
import max7219.led as led     #import the max7219 library
device = led.matrix()
device.show_message("Hello Edkits")
#end of code
                    
