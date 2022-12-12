import math

some_centuries = int(input())

years = some_centuries * 100
days = math.floor(years * 365.2422)
hours = days * 24
minutes = hours * 60


print(f"{some_centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")