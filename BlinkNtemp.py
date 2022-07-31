import utime
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
#power = Pin(36, Pin.OUT)
#timer = Timer()
#timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)
# def blink(timer):
#     led.toggle()
# total = "10"
# x = "0"
# for x in total:
#     led.toggle()
# 
sensor_temp = machine.ADC(4)

#If you print the value of the temperature value you
#are going to get an integer number between 0 and 65535.
#So, we have to convert this value either to the Celsius
#or Fahrenheit degree scales.
conversion_factor = 3.3 / (65535)
#The temperature sensor works by delivering a voltage
#to the ADC4 pin that is proportional to the temperature.
#From the datasheet, a temperature of 27 degrees Celsius
#delivers a voltage of 0.706 V. With each additional
#degree the voltage reduces by 1.721 mV or 0.001721 V.
#The first step in converting the 16-bit temperature is
#to convert it back to volts, which is done based on the
#3.3 V maximum voltage used by the Pico board.
#power.toggle()
while True:
    led.toggle()
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature,'c')
    utime.sleep(.1)