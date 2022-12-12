import math

r = float(input())

area = math.pi * r * r
perimeter = 2 * math.pi * r

print("{:.2f}".format(area))
print("{:.2f}".format(perimeter))