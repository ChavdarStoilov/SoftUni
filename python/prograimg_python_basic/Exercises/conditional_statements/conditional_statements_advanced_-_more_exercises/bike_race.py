count_juniors = int(input())
count_seniors = int(input())
type_trace = str(input())

tax = 0

if type_trace == "trail":
    tax += count_juniors * 5.50 + count_seniors * 7

elif type_trace == "cross-country":
    if count_juniors + count_seniors >= 50:
        discount = ((count_juniors * 8) + (count_seniors * 9.50))* 0.25
        tax += ((count_juniors * 8) + (count_seniors * 9.50)) - discount
    else:
        tax += count_juniors * 8 + count_seniors * 9.50

elif type_trace == "downhill":
    tax += count_juniors * 12.25 + count_seniors * 13.75

else:
    tax += count_juniors * 20 + count_seniors * 21.50


costs = tax * 0.05
end_sum = tax - costs

print("{:.2f}".format(end_sum))