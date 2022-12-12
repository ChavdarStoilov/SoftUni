import math

serial = str(input())
need_time = int(input())
break_time = int(input())

eating = break_time / 8
chill = break_time / 4

left_time = break_time - eating - chill

if need_time <= left_time:
    left = left_time - need_time
    print(f"You have enough time to watch {serial} and left with {math.ceil(left)} minutes free time.")

elif need_time > left_time:
    need = need_time - left_time
    print(f"You don't have enough time to watch {serial}, you need {math.ceil(need)} more minutes.")