from microbit import *
import neopixel
import time
from random import randint
from lcd_i2c import LCD1602

lcd = LCD1602()

NP_LED_COUNT_0 = 30

# Neopixel on pin0
np_0 = neopixel.NeoPixel(pin0, NP_LED_COUNT_0)


def terrain():
    led_rouge = [0, 29]
    led_orange = [1, 2, 27, 28]
    led_verte = [3, 4, 5, 24, 25, 26]

    for led in led_rouge:
        np_0[led] = (255, 0, 0)

    for led in led_orange:
        np_0[led] = (255, 130, 0)

    for led in led_verte:
        np_0[led] = (0, 255, 0)

    np_0.show()
    

def ecran_lcd():
  lcd.clear()
  lcd.setCursor(0, 0)
  lcd.writeTxt('J1 : ')
  lcd.setCursor(0, 1)
  lcd.writeTxt('J2 : ')


def balle_gauche(delta, start):
    for i in range(start, NP_LED_COUNT_0):
        color = np_0[i]
        np_0[i] = (200, 200, 200)
        np_0.show()
        time.sleep(delta)
        np_0[i] = color
        np_0.show()
        if button_b.was_pressed():
          return i


def balle_droite(delta, start):
    for i in range(start, -1, -1):
        color = np_0[i]
        np_0[i] = (200, 200, 200)
        np_0.show()
        time.sleep(delta)
        np_0[i] = color
        np_0.show()
        if button_a.was_pressed():
          return i


def eteindre(temps):
    time.sleep(temps)

    for i in range(NP_LED_COUNT_0):
        np_0[i] = (0, 0, 0)

    np_0.show()


def service_depart():
  nombre = randint(1,2)
  i = None
  if nombre == 1:
    i = balle_droite(0.15, 14)
    return True, i
  else:
    i = balle_gauche(0.15, 14)
    return False, i

def jeu():
  terrain()
  droite, i = service_depart()
  
  while True:
    if droite:
      droite = False
      i = balle_gauche(0.3, i)
    else:
      droite = True
      i = balle_droite(0.3, i)
      eteindre(1)


if __name__ == "__main__":
  terrain()
  ecran_lcd()
  service_depart()
  eteindre(60)
  
