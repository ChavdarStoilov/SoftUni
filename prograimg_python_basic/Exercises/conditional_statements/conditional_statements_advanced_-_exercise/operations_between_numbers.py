n1 = int(input())
n2 = int(input())
operator = input()

result = ""
sum = 0

if n2 == 0:
    print(f"Cannot divide {n1} by zero")

# •	Ако операцията е модулно деление
elif operator == "%":
    sum = n1 % n2

# •	Ако операцията е събиране, изваждане или умножение:
elif operator == "+":
    sum = n1 + n2
    if sum % 2 == 0:
        result = "even"
    else:
        result = "odd"

elif operator == "-":
    sum = n1 - n2
    if sum % 2 == 0:
        result = "even"
    else:
        result = "odd"

elif operator == "*":
    sum = n1 * n2
    if sum % 2 == 0:
        result = "even"
    else:
        result = "odd"

# •	Ако операцията е деление:
elif operator == "/":
    sum = "{:.2f}".format(n1 / n2)

if result == "" and n2 != 0:
    print(f"{n1} {operator} {n2} = {sum}")

elif result == "even" or result == "odd" and n2 != 0:
    print(f"{n1} {operator} {n2} = {sum} - {result}")
