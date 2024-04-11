from microbit import *
import neopixel
import time

NP_LED_COUNT_0 = 30

# Neopixel on pin0
np_0 = neopixel.NeoPixel(pin0, NP_LED_COUNT_0)


def terrain():
    led_rouge = [0, 1, 28, 29]
    led_orange = [2, 3, 4, 25, 26, 27]
    led_verte = [5, 6, 7, 8, 9, 20, 21, 22, 23, 24]

    for led in led_rouge:
        np_0[led] = (255, 0, 0)

    for led in led_orange:
        np_0[led] = (255, 255, 0)

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
eteindre(1)


terrain()
eteindre(60)