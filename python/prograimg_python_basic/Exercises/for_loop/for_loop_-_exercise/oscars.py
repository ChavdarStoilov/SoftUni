import sys

actor_name = str(input())
points_of_academy = float(input())
count_jury = int(input())

result = points_of_academy

for points in range(count_jury):
    name_of_judge = str(input())
    points_of_judge = float(input())
    result += (len(name_of_judge) * points_of_judge) / 2
    if result > 1250.5:
        break


if result > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {result:.1f}!")
else:
    need_more = 1250.5 - result
    print(f"Sorry, {actor_name} you need {need_more:.1f} more!")