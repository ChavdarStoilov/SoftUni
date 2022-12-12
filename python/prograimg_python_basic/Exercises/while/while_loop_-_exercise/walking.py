step = input()

steps = 0

while step != "Going home":
    walking = int(step)
    steps += walking
    if steps > 10000:
        break

    step = input()



if steps >= 10000:
    over_steps = steps - 10000
    print(f"Goal reached! Good job!\n{over_steps} steps over the goal!")
else:
    steps_to_home = int(input())
    sum = steps + steps_to_home
    if sum >= 10000:
        over_steps = abs(10000 - sum)
        print(f"Goal reached! Good job!\n{over_steps} steps over the goal!")
    else:
        more_steps = abs(10000 - steps - steps_to_home)
        print(f"{more_steps} more steps to reach goal.")