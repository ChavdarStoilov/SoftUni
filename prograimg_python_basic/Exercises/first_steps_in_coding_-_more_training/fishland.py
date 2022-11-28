price_mackerel_per_kg = float(input())
price_sprat_per_kg = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = int(input())


price_bonito = price_mackerel_per_kg * 0.60
price_scad = price_sprat_per_kg * 0.80
mussels = 7.50

sum_bonito = (price_mackerel_per_kg + price_bonito) * bonito_kg
sum_scad = (price_sprat_per_kg + price_scad) * scad_kg
sum_mussels = mussels * mussels_kg

end_sum = sum_scad + sum_mussels + sum_bonito
print("{:.2f}".format(end_sum))