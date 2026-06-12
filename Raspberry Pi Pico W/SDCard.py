from machine import RTC
import time
import utime

def log_event(count):
    t = rtc.datetime()

    timestamp = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        t[0], t[1], t[2], t[4], t[5], t[6]
    )

    line = "{} | {x -type of detection radiation}: {}\n".format(timestamp, count)

    # Save to SD card
    with open("/sd/x_log.txt", "a") as f:
        f.write(line)
