from terrain import *
from microbit import *
import neopixel
import time
from random import randint

NP_LED_COUNT_0 = 30

# Neopixel on pin0
np_0 = neopixel.NeoPixel(pin0, NP_LED_COUNT_0)


def on_start():
    terrain()
    return service_depart()


def game(droite, i):

    compteur_jd = 0
    compteur_jg = 0

    while compteur_jd < 11 and compteur_jg < 11:

        # balle gauche → droite
        if droite:
            # result = i si bonne balle False sinon
            result = balle_droite(0.15, i)

            if not result:
                compteur_jd += 1
                droite, i = service_depart()
            else:
                i = result
                droite = False

        # baller droite -> gauche
        else:
            # result = i si bonne balle False sinon
            result = balle_gauche(0.15, i)

            if not result:
                compteur_jg += 1
                droite, i = service_depart()
            else:
                i = result
                droite = True

    eteindre(5)


if __name__ == '__main__':
    sens, i = on_start()
    game(sense, i)
