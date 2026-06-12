#### from machine import Pin    - Importing micropython library which give as possibility to communicate board PI Pico W over PINs with LED diode
#### from utime import sleep    - Importing micropython library which give as possibility to create a time pause in MicroPython in number of seconds

#### led = Pin(5, Pin.OUT)      - In variable led we put output of function Pin. Number 5 in bracket mean pin number on Rassberry Pi pico board and Pin.OUT mean we send signal on LED diode which is conetct with board over that pin.

#### while TRUE: - Create infinite loop

#### led.toggle() - Change value of Pin ( 1 mean on and 2 mean off) which affect LED diode turn on or turn off state

#### sleep(0.5) - Create a time pause in MicroPython in number of seconds
