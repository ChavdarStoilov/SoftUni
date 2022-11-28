nylon = int(input()) + 2
paint = int(input())
thinner = int(input()) * 5.00
hours = int(input())

sum_nylon = nylon * 1.50
sum_pain = (paint + (paint * (10 / 100))) * 14.50

sum_materials = (sum_nylon + sum_pain + thinner + 0.40)
sum = (sum_materials * (30 / 100)) * hours
end_sum = sum_materials + sum
print(end_sum)