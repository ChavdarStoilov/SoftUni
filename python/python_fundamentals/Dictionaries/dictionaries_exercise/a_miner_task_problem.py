command = input()
line = 0
miner_task = {}
the_resource = ""
quantity = 0

while command != "stop":
    line += 1
    some_string = command


    if line % 2 == 0:
        quantity = int(some_string)
        if the_resource in miner_task:
            miner_task[the_resource] += quantity
        else:
            miner_task[the_resource] = quantity
        the_resource = ""
        quantity = 0
    elif line % 2 != 0:
        the_resource = some_string



    command = input()

for resource, value in miner_task.items():
    print(f"{resource} -> {value}")