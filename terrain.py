from microbit import *
import neopixel
import time

NP_LED_COUNT_0 = 30

# Neopixel on pin0
np_0 = neopixel.NeoPixel(pin0, NP_LED_COUNT_0)


def terrain():
  
  led_rouge = [0,29]
  led_orange = [1, 2, 27, 28]
  led_verte = [3, 4, 5, 24, 25, 26]
  
  for led in led_rouge:
    np_0[led] = (255, 0, 0)
  

  for led in led_orange:
    np_0[led] = (220, 100, 0)
  


  for led in led_verte:
    np_0[led] = (0, 255, 0)
  
  np_0.show()
  


def eteindre(temps):
  time.sleep(temps)
  
  for i in range(NP_LED_COUNT_0):
    np_0[i] = (0, 0, 0)
  
  np_0.show()
  
def balle_gauche(delta, start):
  
  for i in range(start, NP_LED_COUNT_0):
    
    color = np_0[i]
    np_0[i] = (200, 200, 200)
    np_0.show()
    time.sleep(delta)
    np_0[i] = color
    np_0.show()
    

def balle_droite(delta, start):
  
  for i in range(start, -1, -1):
    
    color = np_0[i]
    np_0[i] = (200, 200, 200)
    np_0.show()
    time.sleep(delta)
    np_0[i] = color
    np_0.show()

terrain()
balle_gauche(0.1, 12)
balle_droite(0.1, 20)
eteindre(1)
