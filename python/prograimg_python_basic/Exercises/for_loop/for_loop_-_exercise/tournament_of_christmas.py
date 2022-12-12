import math

count_of_tournaments = int(input())
first_points = int(input())

points_from_tournaments = 0
count_win = 0

for tournaments in range(count_of_tournaments):
    type_of_match = str(input())

    if type_of_match == "W":
        points_from_tournaments += 2000
        count_win += 1
    elif type_of_match == "F":
        points_from_tournaments += 1200
    else:
        points_from_tournaments += 720

end_points = points_from_tournaments + first_points
print(f"Final points: {end_points}")
average = math.floor((points_from_tournaments / count_of_tournaments))
print(f"Average points: {average}")
percentage_win = (count_win / count_of_tournaments) * 100
print(f"{percentage_win:.2f}%")
