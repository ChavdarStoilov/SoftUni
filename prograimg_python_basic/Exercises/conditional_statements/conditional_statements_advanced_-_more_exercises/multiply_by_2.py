for test in range(30):
    number = float(input())
    if number > 0 or number == 0:
        result = number * 2
        print(f"Result: {result:.2f}")
        continue
    else:
        print("Negative number!")
        break