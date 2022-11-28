x = float(input())
y = float(input())
h = float(input())


door_x = 1.2 * 2
window_x = 1.5 * 1.5

walls = ((x * y) * 2) - (window_x * 2)
rear_and_front_walls = ((x * x)*2) - door_x

area_walls = walls + rear_and_front_walls
green = area_walls / 3.4

roof = (x * y) * 2
rear_and_front_roof = ((x * h / 2) * 2)
area_roof = roof + rear_and_front_roof
red = area_roof / 4.3

print("{:.2f}".format(green))
print("{:.2f}".format(red))
