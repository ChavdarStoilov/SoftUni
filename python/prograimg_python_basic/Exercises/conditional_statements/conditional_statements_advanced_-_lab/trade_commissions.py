city = str(input())
sales = float(input())

commission = 0

if 0 <= sales <= 500:
    if city == "Sofia":
        commission = 0.05
        print("{:.2f}".format(sales * commission))
    elif city == "Varna":
        commission = 0.045
        print("{:.2f}".format(sales * commission))
    elif city == "Plovdiv":
        commission = 0.055
        print("{:.2f}".format(sales * commission))
    else:
        print("error")

elif 500 <= sales <= 1000:
    if city == "Sofia":
        commission = 0.07
        print("{:.2f}".format(sales * commission))
    elif city == "Varna":
        commission = 0.075
        print("{:.2f}".format(sales * commission))
    elif city == "Plovdiv":
        commission = 0.08
        print("{:.2f}".format(sales * commission))
    else:
        print("error")

elif 1000 <= sales <= 10000:
    if city == "Sofia":
        commission = 0.08
        print("{:.2f}".format(sales * commission))
    elif city == "Varna":
        commission = 0.10
        print("{:.2f}".format(sales * commission))
    elif city == "Plovdiv":
        commission = 0.12
        print("{:.2f}".format(sales * commission))
    else:
        print("error")

elif sales > 10000:
    if city == "Sofia":
        commission = 0.12
        print("{:.2f}".format(sales * commission))
    elif city == "Varna":
        commission = 0.13
        print("{:.2f}".format(sales * commission))
    elif city == "Plovdiv":
        commission = 0.145
        print("{:.2f}".format(sales * commission))
    else:
        print("error")

else:
    print("error")