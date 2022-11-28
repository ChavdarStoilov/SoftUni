exam_hour = int(input())
exam_minute = int(input())
appear_hour = int(input())
appear_minute = int(input())

result = ""
hours = 0
minutes = 0
type_result = ""

exam_hours_in_minutes = (exam_hour * 60) + exam_minute
appear_hour_in_minutes = (appear_hour * 60) + appear_minute

time1 = abs(appear_hour_in_minutes - exam_hours_in_minutes)

if exam_hours_in_minutes < appear_hour_in_minutes:
    print("Late")
    if time1 >= 60:
        hour = time1 // 60
        min = time1 % 60
        if min < 10:
            print(f"{hour}:0{min} hours after the start")
        else:
            print(f"{hour}:{min} hours after the start")
        print(f"{time1} minutes after the start")

    else:
        print(f"{time1} minutes after the start")

elif exam_hours_in_minutes == appear_hour_in_minutes or time1 <= 30:
    print("On time")
    if 1 <= time1 <= 30:
        print(f"{time1} minutes before the start")

else:
    print("Early")
    if time1 >= 60:
        hour = time1 // 60
        min = time1 % 60
        if min < 10:
            print(f"{hour}:0{min} hours before the start")
        else:
            print(f"{hour}:{min} hours before the start")
        print(f"{time1} minutes before the start")
    else:
        print(f"{time1} minutes before the start")