from machine import ADC, Pin
import utime
import time
import _thread

#adc = ADC(Pin(26))
led = Pin(25,Pin.OUT)
led1 = Pin(0,Pin.OUT)
led2 = Pin(1,Pin.OUT)
led3 = Pin(2,Pin.OUT)
led4 = Pin(3,Pin.OUT)
rotoryDT = Pin(16, Pin.IN, Pin.PULL_UP)
rotoryCLK = Pin(17, Pin.IN, Pin.PULL_UP)
button_pin = Pin(18, Pin.IN, Pin.PULL_UP)
previous_value = True
button_down = False
delay = 0.1

#def pot_thread():
    #while True:
        #print(adc.read_u16())

#_thread.start_new_thread(pot_thread, ())

while True:
    print("dir", rotoryDT.value(), "step", rotoryCLK.value())
    if previous_value != rotoryCLK.value():
         if rotoryCLK.value() == False:
             if rotoryDT.value() == False:
                 print("turned left")
             else:
                 print("turned right")
         previous_value = rotoryCLK.value()
    if button_pin.value() == False and not button_down:
         print("button pushed") 
         button_down = True
    if button_pin.value() == True and button_down:
         button_down = False

    if button_pin.value() == False:
         print("button pressed")
    led.toggle()
    led1.high()
    utime.sleep(delay)
    led1.low()
    led2.high()
    utime.sleep(delay)
    led2.low()
    led3.high()
    utime.sleep(delay)
    led3.low()
    led4.high()
    utime.sleep(delay)
    led4.low()