# # from abc import ABC, abstractmethod
# #
# #
# # class Email(ABC):
# #
# #     def __init__(self):
# #         pass
# #
# #
# # class SendEmail(ABC):
# #     pass
# #
#
# ds = ['1', 'asd', 'asdas', '4']
# result = {ds.index(d): d for d in ds if d.isdigit()}
# print(result[3])

from calendar import monthrange

moths = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
years = []

the_expect_blossom = input().split()
days, month, year = int(the_expect_blossom[0]), the_expect_blossom[1], int(the_expect_blossom[2])
mont_num = [num for num, mont in moths.items() if month == mont]
num_days = monthrange(year, mont_num[0])[1]

avg_temp = int(input())
rain = int(input())
winter_days = int(input())


winter_days_to_week = winter_days // 7
days += winter_days_to_week

if (year % 400 == 0) and (year % 100 == 0):
    avg_temp += 5
elif (year % 4 ==0) and (year % 100 != 0):
    avg_temp += 5


if avg_temp >= 20:
    add_more = avg_temp - 20
    while add_more != 0:
        days -= 1
        if days < 1:
            month = moths[mont_num[0] - 1]
            days = num_days = monthrange(year, mont_num[0] - 1)[1]
        add_more -= 1


elif avg_temp < 20:
    add_more = avg_temp - 20
    while add_more != 0:
        days += 1
        if days > num_days:
            days = 1
            month = moths[mont_num[0] + 1]
        add_more -= 1

if rain < 30:
    while rain < 30:
        rain += 3
        days += 1
        if days > num_days:
            days = 1
            month = moths[mont_num[0] + 1]

elif rain > 30:
    while rain > 30:
        rain += 3
        days += 1
        if days > num_days:
            days = 1
            month = moths[mont_num[0] + 1]



print(f'{days} {month} {year}')


"""катеригоризация на егн не на сим
динамични полета в sms
тайминг на стъпките"""