from machine import Pin
import utime

rotoryDT = Pin(16, Pin.IN, Pin.PULL_UP)
rotoryCLK = Pin(17, Pin.IN, Pin.PULL_UP)
rotoryBTN = Pin(18, Pin.IN, Pin.PULL_UP)
LEDList = [Pin(25,Pin.OUT),Pin(0,Pin.OUT),Pin(1,Pin.OUT),Pin(2,Pin.OUT),Pin(3,Pin.OUT)]
listSize = len(LEDList)
previousPosition = 1
currentPosition = 0

def rotory_dial():
    global previousPosition
    global currentPosition
    
    if previousPosition != rotoryCLK.value():
        if rotoryCLK.value() == 0:
            if rotoryDT.value() ==0:
                currentPosition = (currentPosition - 1)%listSize
                print("Rotating Left", currentPosition)
            else:
                currentPosition = (currentPosition + 1)%listSize
                print("Rotating Right", currentPosition)
        previousPosition = rotoryCLK.value()


    if rotoryBTN.value() == 0:
        for x in range(0,listSize): #when pressed all will light up
            LEDList[x].high()
            utime.sleep(.01)
            LEDList[x].low()
        print("Depressed Button is sad!")
        utime.sleep(.001)
    else:
        pass


while True:
    for i in range (0,listSize):
        LEDList[i].value(0)
        rotory_dial()
        LEDList[currentPosition].value(1)
        utime.sleep(.001)      
#from machine import ADC
#import time
#import _thread #for multithreading because pico is dual core

#adc = ADC(Pin(26))
#led = Pin(25,Pin.OUT)
#led1 = Pin(0,Pin.OUT)
#led2 = Pin(1,Pin.OUT)
#led3 = Pin(2,Pin.OUT)
#led4 = Pin(3,Pin.OUT)
#previous_value = True
#button_down = False
#delay = 0.1

#while True:
    #print("dir", rotoryDT.value(), "step", rotoryCLK.value())
    #if previous_value != rotoryCLK.value():
         #if rotoryCLK.value() == False:
             #if rotoryDT.value() == False:
                 #print("turned left")
             #else:
                 #print("turned right")
         #previous_value = rotoryCLK.value()
    #if rototryBTN.value() == False and not button_down:
         #print("button pushed") 
         #button_down = True
    #if rototryBTN.value() == True and button_down:
         #button_down = False

    #if rototryBTN.value() == False:
         #print("button pressed")
    #led.toggle()
    #led1.high()
    #utime.sleep(delay)
    #led1.low()
    #led2.high()
    #utime.sleep(delay)
    #led2.low()
    #led3.high()
    #utime.sleep(delay)
    #led3.low()
    #led4.high()
    #utime.sleep(delay)
    #led4.low()