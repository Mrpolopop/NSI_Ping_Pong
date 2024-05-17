from microbit import *
import radio

radio.on()
radio.config(channel = 12, power = 6, length = 32, group=12)

display.show("D")

while True:
  if button_a.is_pressed():
    radio.on()
    radio.send("bouton_B")
    radio.off()
