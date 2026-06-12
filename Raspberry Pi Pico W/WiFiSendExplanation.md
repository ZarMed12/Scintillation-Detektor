##### from machine import RTC - machine time

##### log_event(count) - Function which write on SD card timestamp and value on that time moment

##### t = rtc.datetime() - Used function datetime() from RTC class

##### timestamp = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(t[0], t[1], t[2], t[4], t[5], t[6]) - Timestamp in next format 2026-06-12 14:30:05 (:04d) mean 4 number which represent year, next 2 numbers represent month... Format of timestamp is year, month, day, hour, minute and second

##### line = "{} | {x - type of detected radiation}: {}\n".format(timestamp, count) - Format of line which will be write in .txt file, can be .csv or other file format. In first empty bracket is store timestamp value, then text description of type of radiation detection particle and in second bracket 

##### try except loop is error catcher which give information if data is not send

##### urequests.post(SERVER_URL, json={"time": timestamp, "type of detected radiation": count}).close() - Sends HTTP POST with JSON body
    
##### print(response.status_code) - Give feedback about not sent data
