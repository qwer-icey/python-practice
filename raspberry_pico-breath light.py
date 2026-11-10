
import time
from machine import Pin, PWM

pwm = PWM(Pin(25))

while True:

    pwm.duty_u16(32768)
    time.sleep(1)
    


  
    
   