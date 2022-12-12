import math

hours = int(input())
day_available = int(input())
count_workers_worked_over_time = int(input())

training = day_available - (day_available * 0.10)
work_time_available_for_the_week = training * 8

work_over_time = count_workers_worked_over_time * (2 * day_available)  # 14 = 2 часа на ден за 7 дена
end_time = work_time_available_for_the_week + work_over_time

if end_time >= hours:
    left_time = math.floor(end_time - hours)
    print(f"Yes!{left_time} hours left.")

else:
    need_more_time = math.ceil(hours - end_time)
    print(f"Not enough time!{need_more_time} hours needed.")
