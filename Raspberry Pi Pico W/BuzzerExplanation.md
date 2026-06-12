##### from machine import Pin    - Importing micropython library which give as possibility to communicate board PI Pico W over PINs with buzzer
##### from utime import sleep    - Importing micropython library which give as possibility to create a time pause in MicroPython in number of seconds

##### buzzer = Pin(15, Pin.OUT)      - In variable buzzer we put output of function Pin. Number 15 in bracket mean pin number on Rassberry Pi pico board and Pin.OUT mean we send signal on buzzer which is conetct with board over that pin.

##### while TRUE: - Create infinite loop

##### buzzer.value(not buzzer.value()) - Change value of Pin ( 1 mean on and 0 mean off) which affect buzzer turn on or turn off state

##### sleep(0.5) - Create a time pause in MicroPython in number of seconds

##### wiring GPIO Pin 15 + side and GND - side 
##### 
