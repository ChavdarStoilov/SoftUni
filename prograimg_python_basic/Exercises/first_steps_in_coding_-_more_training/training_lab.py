w = float(input())
h = float(input())


hall_width = int(w * 100)
hall_length = int(h * 100)
corridor = 100
work_place_wight = 70
work_place_length = 120
department_wight = 160
department_length = 120

possible_desk_per_row = (hall_length - corridor) // work_place_wight
rows = hall_width // work_place_length

end_desk = (possible_desk_per_row * rows) - 3
print(end_desk)