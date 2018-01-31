#brings in time
import time
start = time.time()
#to make sensors work
import setup
import RoboPiLib as RPL
#sensor pin reading
pin = raw_input("What is the pin number? ")
#to make definable in a function
close = RPL.digitalRead(pin)
#which pin the motor is in
motorL = 1
mororR = 0
#it runs when the pin is not reading anything
while close is 1:
    RPL.servoWrite(mororL, 1000)
    RPL.servoWrite(motorR, 2000)
#it stops when the sensor senses something
else:
    RPL.servoWrite(mororL, 0)
    RPL.servoWrite(motorR, 0)
    return
#write code to slow down robot
end = time.time()
