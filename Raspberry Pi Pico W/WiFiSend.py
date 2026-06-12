import network
import urequests
import time
import utime
from machine import RTC

def log_event(count):
    t = rtc.datetime()

    timestamp = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        t[0], t[1], t[2], t[4], t[5], t[6]
    )

    line = "{} | {x -type of detection radiation}: {}\n".format(timestamp, count)
   
    try:
        urequests.post(SERVER_URL, json={
            "time": timestamp,
            "muons": count
        }).close()
    except:
        print(response.status_code)
