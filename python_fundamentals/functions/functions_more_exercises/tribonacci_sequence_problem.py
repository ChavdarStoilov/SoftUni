def printTribRec(n):
    if (n == 1 or n == 2 or n == 3):
        return 1
    elif (n == 3):
        return 2
    else:
        return (printTribRec(n - 1) +
                printTribRec(n - 2) +
                printTribRec(n - 3))


def printTrib(n):
    for i in range(1, n):
        print(printTribRec(i), " ", end="")


# Driver code
n = 4
printTrib(n)