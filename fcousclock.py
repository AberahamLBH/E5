
import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds >0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

focus_timer(25) # 25分钟专注时间
