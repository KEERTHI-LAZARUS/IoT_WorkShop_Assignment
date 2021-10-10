import machine

cpin=machine.Pin(2,machine.Pin.OUT)
pwm=machine.PWM(cpin)
pwm.freq(50)
pwm.duty(0)

def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def servo(angle):
    if x==1:
        pwm.duty(map(angle, 0, 180, 20, 120))
    else:
        pwn.duty(map(angle,180,0,20,120))
    
print("Enter 1 for CLOCKWISE // Enter 2 for ANTI-CLOCKWISE")
x=input("enter 1 or 2")
angle=input("enter the angle")
