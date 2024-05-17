from microbit import *
import radio

radio.on()
radio.config(channel = 12, power = 6, length = 32, group=12)

display.show("G")
while True:
  if button_a.is_pressed():
    radio.send("A")
