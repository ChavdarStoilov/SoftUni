divisor_number = int(input())
boundary_number = int(input())

max_number = []

for n in range(divisor_number, boundary_number + 1):
    if n % divisor_number == 0 and boundary_number >= n > 0:
        max_number.append(n)

print(max(max_number))