price_fruit_per_kg = float(input())
price_vegetables_per_kg = float(input())
sum_kg_fruit = float(input())
sum_kg_vegetables = float(input())

sum_fruit = price_fruit_per_kg * sum_kg_fruit
sum_vegetables = price_vegetables_per_kg * sum_kg_vegetables

end_sum = (sum_fruit + sum_vegetables) / 1.94
print("{:.2f}".format(end_sum))