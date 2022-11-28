budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())
per = 0

if video_cards > processors:
    per = 0.15

video_price = 250
buy_cards = video_cards * video_price
processor_price = buy_cards * 0.35
ram_price = buy_cards * 0.10

buy_processor = processors * processor_price
buy_ram = ram * ram_price

end_price = (buy_ram + buy_processor + buy_cards) * per
end_sum = (buy_ram + buy_processor + buy_cards) - end_price

if end_sum > budget:
    need_more = end_sum - budget
    print("Not enough money! You need " + "{:.2f}".format(need_more) + " leva more!")

elif end_sum <= budget:
    left = budget - end_sum
    print("You have " + "{:.2f}".format(left) + " leva left!")