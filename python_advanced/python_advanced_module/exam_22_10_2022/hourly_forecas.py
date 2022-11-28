def forecast(*args):
    weathers = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    for locations in args:
        location = locations[0]
        weather = locations[1]

        weathers[weather].append(location)

    # sort = sorted(weathers.items(), key= lambda x: x[1])

    end_result = ''
    for the_weather, the_locations in weathers.items():
        for the_location in sorted(the_locations):
            end_result += f'{the_location} - {the_weather}\n'

    return end_result

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
