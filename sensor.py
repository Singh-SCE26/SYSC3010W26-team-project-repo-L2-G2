from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

FULL_NAME = "Aryan Singh"  # change if needed
SCROLL_SPEED = 0.06

while True:
    sense.show_message(FULL_NAME, scroll_speed=SCROLL_SPEED)
    time.sleep(0.25)
