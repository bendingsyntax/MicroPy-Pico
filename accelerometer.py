from imu import MPU6050
from machine import Pin, I2C
import time

accelSCL = Pin(15, Pin.OUT)
accelSDA = Pin(14, Pin.OUT)
accelI2C = I2C(1, sda=accelSDA, scl=accelSCL, freq=400000)
LEDList = [Pin(25,Pin.OUT),Pin(0,Pin.OUT),Pin(1,Pin.OUT),Pin(2,Pin.OUT),Pin(3,Pin.OUT)]
imu = MPU6050(accelI2C)

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
    #stringAxis = "x axis" + ax + "\t"+ "y axis"+ ay+"\t"+ "z axis"+ az
    #stdscr.addstr(0, 0,stringAxis)
    print("x axis" , ax , "\t", "y axis", ay, "\t", "z axis", az, end="\n")
    print("acceleration on x", gx,"\t", "acceleration on y", gy,"\t", "acceleration on z", gz, end="\n")
    print("Temp:", temp," ", "C", end="\n")
    time.sleep(0.001)
    
#print('Scan i2c bus...')
#i2cDevs = accelI2C.scan()

#if len(i2cDevs) == 0:
#    print("No i2c device !")
#else:
#    print('i2c devices found:',len(i2cDevs))

#for i2cDevs in i2cDevs:
#    print("Decimal address: ",i2cDevs," | Hexa address: ",hex(i2cDevs))