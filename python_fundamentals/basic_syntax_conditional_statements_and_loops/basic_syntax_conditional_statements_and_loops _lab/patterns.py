number = int(input())


for i in range(number + 1):
    print(i * "*")

for c in range(number -1, -1, -1):
    print(c * "*")

#
# for i in range(number + 1):
#     for a in range(0, i):
#         print("*", end="")
#     print()
#
# for i in range(number -1, 0, -1):
#     for a in range(0, i):
#         print("*", end="")
#     print()