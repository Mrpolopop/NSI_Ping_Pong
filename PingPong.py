from microbit import *
import neopixel
import time
from random import randint
from lcd_i2c import LCD1602

lcd = LCD1602()

lcd.clear()
lcd.setCursor(0, 0)
lcd.writeTxt('J1 : ')
lcd.setCursor(0, 1)
lcd.writeTxt('J2 : ')

"""
VARIABLES :
Définition de chaque led dans la bande ainsi que les zones vertes, oranges et rouges.
"""

NP_LED_COUNT_0 = 30
np_0 = neopixel.NeoPixel(pin0, NP_LED_COUNT_0)

led_rouge = [1, 28]
led_orange = [2, 3, 26, 27]
led_verte = [4, 5, 6, 23, 24, 25]
led_rouge_d = [1]
led_rouge_g = [28]
led_orange_d = [2, 3]
led_orange_g = [26, 27]
led_verte_d = [4, 5, 6]
led_verte_g = [23, 24, 25]


"""
FONCTIONS : 
"""


def terrain():
    """
    Cette fonction s'occupe d'afficher le terrain défini précédemment sur la bande led
    """

    for led in led_rouge:
        np_0[led] = (255, 0, 0)

    for led in led_orange:
        np_0[led] = (255, 130, 0)

    for led in led_verte:
        np_0[led] = (0, 255, 0)

    np_0.show()


def balle_gauche(delta, start):
    """
    :param delta: une vitesse variable que prend la balle au moment où elle
     sera renvoyée vers la gauche selon la zone où elle a été interceptée.
    :param start: La position d'où part la balle
    :return: va renvoyer une liste comprennant la vitesse que la
    balle aura ainsi que sa position
    """
    # de gauche à droite
    for i in range(start, NP_LED_COUNT_0):

        # affichage
        color = np_0[i]
        np_0[i] = (200, 200, 200)
        np_0.show()
        time.sleep(delta)
        np_0[i] = color
        np_0.show()

        # Détermine en fonction de la zone dans laquelle on la renvoie la vitesse que prendra
        # la balle -> zone verte = lente, zone orange = rapide, zone rouge = très rapide
        if button_a.is_pressed():
            if i in led_verte_g:
                return [i, 0.10]

            elif i in led_orange_g:
                return [i, 0.07]

            elif i in led_rouge_g:
                if delta == 0.04:
                  return 'smash'
                else:
                  return [i, 0.04]
                    
            else:
                return False

        elif i == 28:
            return False


def balle_droite(delta, start):
    """
    :param delta: une vitesse variable que prend la balle au moment où elle
    sera renvoyée vers la droite selon la zone où elle a été interceptée.
    :param start: La position d'où part la balle
    :return: va renvoyer une liste comprennant la vitesse que la
    balle aura ainsi que sa position
    """
    # de droite à gauche
    for i in range(start, -1, -1):

        # affichage
        color = np_0[i]
        np_0[i] = (200, 200, 200)
        np_0.show()
        time.sleep(delta)
        np_0[i] = color
        np_0.show()

        # Détermine en fonction de la zone dans laquelle on la renvoie la vitesse que prendra
        # la balle -> zone verte = lente, zone orange = rapide, zone rouge = très rapide
        if button_b.is_pressed():
            if i in led_verte_d:
                print('droite')
                return [i, 0.1]

            elif i in led_orange_d:
                return [i, 0.07]

            elif i in led_rouge_d:
                if delta == 0.04:
                  return 'smash'
                else:
                  return [i, 0.04]

            else:
                return False

        elif i == 1:
            return False


def eteindre(temps):
    """
    Cette fonction sert à éteindre la bande led afin qu'elle ne soit pas en fonctionnement
    après son utilisation, après un test ou une partie
    :param temps: Valeur qui détermine au bout de combien de temps la bande led s'éteint
    """
    time.sleep(temps)

    # toutes les leds perdent leur couleur donc s'éteindront quand on affichera cela
    for i in range(NP_LED_COUNT_0):
        np_0[i] = (0, 0, 0)

    # affiche donc l'exécution ci dessus et éteint les leds
    np_0.show()
    lcd.clear()


def service_depart():
    """
    :return: Fonction qui sert à faire un service qui enverra la balle
    dans une direction aléatoire
    """
    # on décide de quel coté la balle va partir
    nombre = randint(1, 2)
    if nombre == 1:
        return True, 14, 0.1
    else:
        return False, 14, 0.1


def smash(droite):
  """
  droite: booléen correspondant au sens d'entrée
  animation du smash
  :return: None 
  """
  if droite:
    for i in range(1, NP_LED_COUNT_0):

        # affichage
        color = np_0[i]
        np_0[i] = (152, 25, 218)
        np_0.show()
        time.sleep(0.03)
        np_0[i] = color
        np_0.show()
        
  else:
    for i in range(28, -1, -1):

        # affichage
        color = np_0[i]
        np_0[i] = (152, 44, 218)
        np_0.show()
        time.sleep(0.03)
        np_0[i] = color
        np_0.show()


"""
LE JEU :
"""


def on_start():
    """
    initialise le terrain et lance le jeu
    """
    terrain()
    return service_depart()


def game(droite, i, delta):

    # On initialise le score des deux joueurs
    compteur_jd = 0
    compteur_jg = 0

    # On pose la condition de jeu pour qu'il s'arrête au bout de 5 points
    while compteur_jd < 5 and compteur_jg < 5:

        # balle de droite à gauche
        if droite:

            # result = i si bonne balle False sinon
            result = balle_droite(delta, i)

            if not result:
                compteur_jd += 1
                droite, i, delta = service_depart()
            
            elif result == 'smash':
                compteur_jg += 1
                smash(droite)
                droite, i, delta = service_depart()
            
            else:
                i = result[0]
                delta = result[1]
                droite = False

        # balle de gauche à droite
        else:
            # result = i si bonne balle False sinon
            result = balle_gauche(delta, i)

            if not result:
                compteur_jg += 1
                droite, i, delta = service_depart()
            
            elif result == 'smash':
                compteur_jg += 1
                smash(droite)
                droite, i, delta = service_depart()
            
            else:
                i = result[0]
                delta = result[1]
                droite = True

        # On affiche ensuite les résultats en temps réel sur le petit écran lcd

        points_jg = 'J1 : ' + str(compteur_jg)
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.writeTxt(points_jg)

        points_jd = 'J2 : ' + str(compteur_jd)
        lcd.setCursor(0, 1)
        lcd.writeTxt(points_jd)

    # Lorsque l'un des joueurs est arrivé au nombre de points requis, on affiche le gagnant
    if compteur_jd == 5:
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.writeTxt('J2 a gagne !! :)')

    else:
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.writeTxt('J1 a gagne !! :)')

    eteindre(5)


if __name__ == '__main__':
    #sense, i, delta = on_start()
    #game(sense, i, delta)
    eteindre(1)
    
