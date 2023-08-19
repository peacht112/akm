import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up! Stay focused!")

if __name__ == "__main__":
    try:
        minutes = int(input("请输入专注时长（分钟）："))
        focus_timer(minutes)
    except ValueError:
        print("无效输入。请输入一个有效的数字。")
