from microbit import *
import neopixel
import time
from random import randint

NP_LED_COUNT_0 = 30

# Neopixel on pin0
np_0 = neopixel.NeoPixel(pin0, NP_LED_COUNT_0)


def terrain():
    led_rouge = [1, 28]
    led_orange = [2, 3, 26, 27]
    led_verte = [4, 5, 6, 23, 24, 25]

    for led in led_rouge:
        np_0[led] = (255, 0, 0)

    for led in led_orange:
        np_0[led] = (255, 130, 0)

    for led in led_verte:
        np_0[led] = (0, 255, 0)

    np_0.show()


# def ecran_lcd():

#  lcd.clear()
#  lcd.getCursor(0, 0)
#  lcd.writeTxt('Joueur 1')


def balle_gauche(delta, start):
    # de droite à gauche
    for i in range(start, NP_LED_COUNT_0):

        # affichage
        color = np_0[i]
        np_0[i] = (200, 200, 200)
        np_0.show()
        time.sleep(delta)
        np_0[i] = color
        np_0.show()

        # event listener
        if button_b.was_pressed():
            return i
        elif i == 29:
            return False


def balle_droite(delta, start):
    # de gauche à droite
    for i in range(start, -1, -1):

        # affichage
        color = np_0[i]
        np_0[i] = (200, 200, 200)
        np_0.show()
        time.sleep(delta)
        np_0[i] = color
        np_0.show()

        # event listener
        if button_a.was_pressed():
            return i
        elif i == 0:
            return False


def eteindre(temps):
    time.sleep(temps)

    for i in range(NP_LED_COUNT_0):
        np_0[i] = (0, 0, 0)

    np_0.show()


def service_depart():
    nombre = randint(1, 2)
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
            if i == False:
                break
            else:
                i = balle_gauche(0.3, i)

        else:
            droite = True
            if i == False:
                break
            else:
                i = balle_droite(0.3, i)


if __name__ == "__main__":
    jeu()
