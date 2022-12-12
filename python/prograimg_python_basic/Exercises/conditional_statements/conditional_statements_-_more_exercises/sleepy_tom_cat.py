not_working_days = int(input())

tom_norm_for_play_per_year = 30000

working_day = 365 - not_working_days
real_time_for_play = (working_day * 63) + (not_working_days * 127)

difference_from_norm = abs(tom_norm_for_play_per_year - real_time_for_play)
difference_from_norm_hour = difference_from_norm // 60
difference_from_norm_minutes = difference_from_norm % 60

if tom_norm_for_play_per_year > real_time_for_play:
    print("Tom sleeps well")
    print(f"{difference_from_norm_hour} hours and {difference_from_norm_minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{difference_from_norm_hour} hours and {difference_from_norm_minutes} minutes more for play")