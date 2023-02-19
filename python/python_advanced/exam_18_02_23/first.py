from collections import deque

textile = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

product = {
    "Patch": [30, 0],
    "Bandage": [40, 0],
    "MedKit": [100, 0]
}



while True:

    if not textile or not medicaments:
        break

    count_sum = textile[0] + medicaments[-1]

    if count_sum == product["Patch"][0]:
        product["Patch"][1] += 1
        textile.popleft()
        medicaments.pop()

    elif count_sum == product["Bandage"][0]:
        product["Bandage"][1] += 1
        textile.popleft()
        medicaments.pop()

    elif count_sum == product["MedKit"][0]:
        product["MedKit"][1] += 1
        textile.popleft()
        medicaments.pop()

    else:
        if count_sum > product["MedKit"][0]:
            product["MedKit"][1] += 1
            textile.popleft()
            medicaments.pop()
            left = count_sum - product["MedKit"][0]
            medicaments[-1] += left

        elif count_sum < product["Patch"][0] or count_sum < product["MedKit"][0] or count_sum < product["Bandage"][0]:
            textile.popleft()
            medicaments.append(medicaments.pop() + 10)

if not textile and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textile:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")


# Print order created items

ordered_product = dict(sorted(product.items(), key=lambda item: (- item[1][1], item[0])))


for product, count in ordered_product.items():

    if count[1] > 0:
        print(f"{product} - {count[1]}")


if medicaments:
    left_medicaments = ', '.join([str(x) for x in reversed(medicaments)])
    print(f"Medicaments left: {left_medicaments}")

if textile:
    left_textile = ', '.join([str(x) for x in textile])
    print(f"Textiles left: {left_textile}")