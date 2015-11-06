import pigpio as GPIO
import atexit

pi = GPIO.pi()
inPin = 4
outPin = 15

def cleanup():
   pi.stop()

# MODES=["INPUT", "OUTPUT", "ALT5", "ALT4", "ALT0", "ALT1", "ALT2", "ALT3"]
pi.set_mode(inPin, GPIO.INPUT)
pi.set_mode(outPin, GPIO.OUTPUT)
pi.write(outPin, 0) # Set pin LOW (default)
atexit.register(cleanup)

while True:
    value = pi.read(inPin)
    if value:
        print "Not Pressed"
        pi.write(outPin, 0) # Set pin LOW
    else:
        print "Pressed"
        pi.write(outPin, 1) # Set pin HIGH

