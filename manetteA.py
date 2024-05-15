from microbit import *
import radio

radio.on()

display.show("G")
while True:
  if button_a.is_pressed():
    radio.send("A")
