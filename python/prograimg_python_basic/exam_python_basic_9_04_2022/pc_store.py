price_for_processor = float(input()) * 1.57
price_for_video_card = float(input()) * 1.57
price_for_ram = float(input()) * 1.57
count_of_ram = int(input())
discount = float(input())

money_for_ram = price_for_ram * count_of_ram
discount_for_processor = price_for_processor - (price_for_processor * discount)
discount_for_video_card = price_for_video_card - (price_for_video_card * discount)
end_need_money = (money_for_ram + discount_for_video_card + discount_for_processor)

print(f"Money needed - {end_need_money:.2f} leva.")