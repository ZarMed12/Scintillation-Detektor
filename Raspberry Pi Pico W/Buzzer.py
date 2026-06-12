from machine import Pin
from utime import sleep

buzzer = Pin(15, Pin.OUT)

while True:
    buzzer.value(not buzzer.value())
    sleep(0.5)
