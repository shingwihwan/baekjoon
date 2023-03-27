# 오븐 시계

current_time = input().split(" ")
require_time = input()

hour = int(current_time[0])
minute = int(current_time[1])

hour = (((hour * 60) + minute + int(require_time)) // 60)
minute = ((hour * 60) + minute + int(require_time)) % 60

if hour > 24:
    hour = hour - 24

if hour == 24:
    print("0" + " " + str(minute))
else:
    print(str(hour) + " " + str(minute))
