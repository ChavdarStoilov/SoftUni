type_projection = str(input())
r = int(input())
c = int(input())

price = 0

if type_projection == "Premiere":
    price = 12.00

elif type_projection == "Normal":
    price = 7.50

elif type_projection == "Discount":
    price = 5.00


print("{:.2f}".format((r * c) * price) + " leva")
