from machine import Pin
from utime import sleep

led = Pin(5, Pin.OUT)

print("Pico LED blink started")

while True:
    led.toogle()
    sleep(0.5)
