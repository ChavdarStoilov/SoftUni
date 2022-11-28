command = input()

balance = 0.0

while inpt != "NoMoreMoney":
    amount = float(inpt)
    if amount < 0:
        print("Invalid operation!")
        break

    balance += amount

    print(f"Increase: {amount:.2f}")

    command = input()
print(f"Total: {balance:.2f}")