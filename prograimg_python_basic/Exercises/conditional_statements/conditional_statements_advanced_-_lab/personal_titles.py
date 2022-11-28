years = float(input())
sex = str(input()).lower()

if years < 16:
    if sex == "m":
        print("Master")

    elif sex == "f":
        print("Miss")

elif years >= 16:
    if sex == "m":
        print("Mr.")

    elif sex == "f":
        print("Ms.")