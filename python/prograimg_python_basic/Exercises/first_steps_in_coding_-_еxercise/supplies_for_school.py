pens = int(input())
markers = int(input())
preparation = int(input())
discount = int(input()) / 100

sum_pens = pens * 5.80
sum_markers = markers * 7.20
sum_preparation = preparation * 1.20

sum_after_discount = (sum_preparation + sum_pens + sum_markers) * discount
end_sum = sum_markers + sum_preparation + sum_pens - sum_after_discount


print(end_sum)