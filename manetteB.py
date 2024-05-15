from microbit import *
import radio

radio.on()
display.show("D")

while True:
  if button_a.is_pressed():
    radio.send("B")
