number_of_snowballs = int(input())

snowball_weight = 0
snowball_time = 0
snowball_quality = 0
snowball_value = 0

for balls in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_of_snowball = int(input())
    quality_of_snowball = int(input())

    max_snowball_value = (weight_of_snowball / time_of_snowball) ** quality_of_snowball

    if max_snowball_value > snowball_value:
        snowball_weight = weight_of_snowball
        snowball_time = time_of_snowball
        snowball_quality = quality_of_snowball
        snowball_value = max_snowball_value

print(f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})")
