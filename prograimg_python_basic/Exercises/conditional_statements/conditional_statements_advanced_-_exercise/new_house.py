type_flower = str(input())
count_flower = int(input())
budget = int(input())

discount = 0

roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.50

end_sum =0

if type_flower == "Roses":
    sum_for_flower = count_flower * roses
    if count_flower > 80:
        discount = 0.10
    sum_discount = (sum_for_flower * discount)
    end_sum = (sum_for_flower - sum_discount)

elif type_flower == "Dahlias":
    sum_for_flower = count_flower * dahlias
    if count_flower > 90:
        discount = 0.15
    sum_discount = (sum_for_flower * discount)
    end_sum = (sum_for_flower - sum_discount)

elif type_flower == "Tulips":
    sum_for_flower = count_flower * tulips
    if count_flower > 80:
        discount = 0.15
    sum_discount = (sum_for_flower * discount)
    end_sum = (sum_for_flower - sum_discount)

elif type_flower == "Narcissus":
    sum_for_flower = count_flower * narcissus
    if count_flower < 120:
        discount = 0.15
    sum_discount = (sum_for_flower * discount)
    end_sum = (sum_for_flower + sum_discount)

elif type_flower == "Gladiolus":
    sum_for_flower = count_flower * gladiolus
    if count_flower < 80:
        discount = 0.20
    sum_discount = (sum_for_flower * discount)
    end_sum = (sum_for_flower + sum_discount)


if budget >= end_sum:
    left = budget - end_sum
    print(f"Hey, you have a great garden with {count_flower} {type_flower} and {'{:.2f}'.format(left)} leva left.")

elif budget < end_sum:
    need_more = end_sum - budget
    print(f"Not enough money, you need {'{:.2f}'.format(need_more)} leva more.")