# main.py —— 你的第一个程序
# 上电后 Pico 会自动运行这个文件

import time
from machine import Pin, PWM

pwm = PWM(Pin(25))

while True:
    for i in range(0,65535,512):
        pwm.duty_u16(i)
        time.sleep(0.01)
    for j in range(65535,0,-512):
        pwm.duty_u16(j)
        time.sleep(0.01)
    
    
# 在这里写：让它闪三下，然后停住不亮
