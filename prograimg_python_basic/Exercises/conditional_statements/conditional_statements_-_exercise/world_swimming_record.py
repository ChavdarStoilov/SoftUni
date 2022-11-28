import math

record_second = float(input())
meters = float(input())
time_second = float(input())

need_time = meters * time_second
water = math.floor(meters / 15) * 12.5

end_time = need_time + water

if end_time < record_second:
    print("Yes, he succeeded! The new world record is " + "{:.2f}".format(end_time) + " seconds.")

elif end_time >= record_second:
    need_more = end_time - record_second
    print("No, he failed! He was " + "{:.2f}".format(need_more) + " seconds slower.")

