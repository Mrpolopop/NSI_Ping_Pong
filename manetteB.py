from microbit import *
import radio
import time

radio.on()
radio.config(channel = 12, power = 6, length = 32, group=12)

display.show("D")
while True:
  if button_a.is_pressed():
    radio.send("bouton_B")
    time.sleep(0.2)
    radio.send("null")
