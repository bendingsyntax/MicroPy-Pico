from imu import MPU6050
from machine import Pin, I2C, PWM
import _thread
import utime

LEDList = [Pin(25,Pin.OUT),Pin(0,Pin.OUT),Pin(1,Pin.OUT),Pin(2,Pin.OUT),Pin(3,Pin.OUT)]
RGBLED = [Pin(4,Pin.OUT),Pin(5,Pin.OUT),Pin(6,Pin.OUT),Pin(7,Pin.OUT),Pin(8,Pin.OUT),Pin(9,Pin.OUT)]
listSize = len(RGBLED)

rotoryDT = Pin(16, Pin.IN, Pin.PULL_UP)
rotoryCLK = Pin(17, Pin.IN, Pin.PULL_UP)
rotoryBTN = Pin(18, Pin.IN, Pin.PULL_UP)
previousPosition = 1
currentPosition = 0

accelSCL = Pin(15, Pin.OUT)
accelSDA = Pin(14, Pin.OUT)
accelI2C = I2C(1, sda=accelSDA, scl=accelSCL, freq=400000)
imu = MPU6050(accelI2C)

MID = 1500000 #1.4ms AKA 45 degree
MIN = 1000000 #1ms AKA 0 degree
MAX = 2000000 #2ms AKA 90 degree

pwm = PWM(Pin(13))
pwm.freq(50)
pwm.duty_ns(MID)


def rotory_dial():
    global previousPosition
    global currentPosition
    
    if previousPosition != rotoryCLK.value():
        if rotoryCLK.value() == 0:
            if rotoryDT.value() ==0:
                currentPosition = (currentPosition - 1)%listSize
                #print("Rotating Left", currentPosition)
            else:
                currentPosition = (currentPosition + 1)%listSize
                #print("Rotating Right", currentPosition)
        previousPosition = rotoryCLK.value()


    if rotoryBTN.value() == 0:
        for x in range(0,listSize): #when pressed all will light up
            RGBLED[x].high()
            utime.sleep(.01)
            RGBLED[x].low()
        #print("Depressed Button is sad!")
        utime.sleep(.001)
    else:
        pass
    
def first_thread():
    while True:
        ax=round(imu.accel.x,3)
        ay=round(imu.accel.y,3)
        az=round(imu.accel.z,3)
        gx=round(imu.gyro.x,3)
        gy=round(imu.gyro.y,3)
        gz=round(imu.gyro.z,3)
        temp=round(imu.temperature)
        if az >= .95:
            LEDList[0].high()
            LEDList[1].low()
            LEDList[2].low()
            LEDList[3].low()
            LEDList[4].low()
        elif az > .80 and az < .95:
            LEDList[0].low()
            LEDList[1].high()
            LEDList[2].low()
            LEDList[3].low()
            LEDList[4].low()
        elif az > .60 and az < .80:
            LEDList[0].low()
            LEDList[1].low()
            LEDList[2].high()
            LEDList[3].low()
            LEDList[4].low()
        elif az > .30 and az < .60:
            LEDList[0].low()
            LEDList[1].low()
            LEDList[2].low()
            LEDList[3].high()
            LEDList[4].low()
        elif az > .10 and az < .30:
            LEDList[0].low()
            LEDList[1].low()
            LEDList[2].low()
            LEDList[3].low()
            LEDList[4].high()
        elif az < .10:
            pwm.duty_ns(MIN)
            utime.sleep(1.1)
            pwm.duty_ns(MAX)
            utime.sleep(1.1)
        utime.sleep(0.001)
        for i in range (0,listSize):
            RGBLED[i].value(0)
            rotory_dial()
            RGBLED[currentPosition].value(1)

#def second_thread():
#    while True:
#        for i in range (0,listSize):
#            RGBLED[i].value(0)
#            rotory_dial()
#            RGBLED[currentPosition].value(1)
#            utime.sleep(.001) 

_thread.start_new_thread(first_thread, ())
#_thread.start_new_thread(second_thread, ())