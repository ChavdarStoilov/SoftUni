hours = int(input())
minutes = int(input())


total_minute = (hours * 60) + minutes + 15

hour = total_minute // 60
minute = total_minute % 60

if hour > 23:
    hour = 0

if minute <= 9:
    print(f"{hour}:0{minute}")

else:
    print(f"{hour}:{minute}")