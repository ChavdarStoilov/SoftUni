price_for_t_short =float(input())
price_needed = float(input())

price_for_shorts = price_for_t_short * 0.75
price_for_socks = price_for_shorts * 0.20
price_boots = (price_for_t_short + price_for_shorts) * 2

sum_without_discount = price_for_t_short + price_for_socks + price_for_shorts + price_boots
end_sum = sum_without_discount - (sum_without_discount * 0.15)

if end_sum >= price_needed:
    print(f"Yes, he will earn the world-cup replica ball!\n"
          f"His sum is {end_sum:.2f} lv.")
else:
    need_more = price_needed - end_sum
    print(f"No, he will not earn the world-cup replica ball.\n"
          f"He needs {need_more:.2f} lv. more.")