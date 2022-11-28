many_number = input().split(", ")

positive_number = [positive for positive in many_number if int(positive) >= 0]
negative_number = [negative for negative in many_number if int(negative) < 0]
even_number = [even for even in many_number if int(even) % 2 == 0]
odd_number = [odd for odd in many_number if int(odd) % 2 != 0]

print(f"Positive: {', '.join(positive_number)}\n"
      f"Negative: {', '.join(negative_number)}\n"
      f"Even: {', '.join(even_number)}\n"
      f"Odd: {', '.join(odd_number)}\n")