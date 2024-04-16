from microbit import *
import neopixel
import time
from random import randint

#############################
####      variables      ####
#############################

NP_LED_COUNT_0 = 30

# Neopixel on pin0
np_0 = neopixel.NeoPixel(pin0, NP_LED_COUNT_0)

led_rouge = [1, 28]
led_orange = [2, 3, 26, 27]
led_verte = [4, 5, 6, 23, 24, 25]
led_rouge_g = [1]
led_rouge_d = [28]
led_orange_g = [2, 3] 
led_orange_d = [26, 27]
led_verte_g = [4, 5, 6]
led_verte_d = [23, 24, 25]


#############################
####      fonctions      ####
#############################

def terrain():
    led_rouge = [1, 28]
    led_orange = [2, 3, 26, 27]
    led_verte = [4, 5, 6, 23, 24, 25]
    led_rouge_d = [1]
    led_rouge_g = [28]
    led_orange_d = [2, 3] 
    led_orange_g = [26, 27]
    led_verte_d= [4, 5, 6]
    led_verte_g = [23, 24, 25]

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
    led_orange_g = [26, 27]
    led_verte_g = [23, 24, 25]
    led_rouge_g = [28]
    # de gauche à droite
    for i in range(start, NP_LED_COUNT_0):

        # affichage
        color = np_0[i]
        np_0[i] = (200, 200, 200)
        np_0.show()
        time.sleep(delta)
        np_0[i] = color
        np_0.show()

        # event listener
        if button_b.is_pressed():
          if i in led_verte_g:
            return [i , 0.12]
          
          elif i in led_orange_g:
            return [i, 0.10]
          
          elif i in led_rouge_g:
            return [i, 0.10]
            
          else:
            return False
          
        elif i == 28:
            return False


def balle_droite(delta, start):
    led_verte_d = [4, 5, 6]
    led_orange_d = [2, 3]
    led_rouge_d = [1]
    # de droite à gauche
    for i in range(start, -1, -1):

        # affichage
        color = np_0[i]
        np_0[i] = (200, 200, 200)
        np_0.show()
        time.sleep(delta)
        np_0[i] = color
        np_0.show()

        # event listener
        if button_a.is_pressed():
          if i in led_verte_d:
            print('droite')
            return [i , 0.12]
          
          elif i in led_orange_d:
            return [i, 0.10]
          
          elif i in led_rouge_d:
            return [i, 0.10]
            
          else:
            return False
          
        elif i == 1:
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
        return True, 14, 0.12
    else:
        return False, 14, 0.12


#################################
####      boucle de jeu      ####
#################################

def on_start():
    terrain()
    return service_depart()


def game(droite, i, delta):

    compteur_jd = 0
    compteur_jg = 0

    while compteur_jd < 11 and compteur_jg < 11:

        # balle droite à gauche
        if droite:
          
            display.show(compteur_jd)
            # result = i si bonne balle False sinon
            result = balle_droite(delta, i)

            if not result:
                compteur_jd += 1
                droite, i, delta = service_depart()
            else:
                i = result[0]
                delta = result[1]
                droite = False

        # baller gauche à droite
        else:
            
            display.show(compteur_jg)
            # result = i si bonne balle False sinon
            result = balle_gauche(delta, i)

            if not result:
                compteur_jg += 1
                droite, i, delta = service_depart()
            else:
                i = result[0]
                delta = result[1]
                droite = True

    eteindre(5)


if __name__ == '__main__':
    sense, i, delta = on_start()
    game(sense, i, delta)
    eteindre(1)
    
    # pb balle continue apres appuit sur bouton 
