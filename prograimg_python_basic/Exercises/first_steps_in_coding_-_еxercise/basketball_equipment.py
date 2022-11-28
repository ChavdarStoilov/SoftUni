sneakers = 40 / 100
outfit = 20 / 100

tax = int(input())

sneaker = tax -(tax * sneakers)
outfit_price = sneaker -(sneaker * outfit)
ball = outfit_price / 4
accessoires = ball / 5
end_sum = tax + sneaker + outfit_price + ball + accessoires
print(end_sum)