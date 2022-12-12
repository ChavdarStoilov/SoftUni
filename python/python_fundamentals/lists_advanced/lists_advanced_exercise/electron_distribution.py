def distribution_func(numbers):
    shells = []

    for electrons in range(1, numbers):
        shells.append(2 * electrons ** 2)
        if sum(shells) == numbers:
            return shells
        elif sum(shells) > numbers:
            for num in range(1, shells[-1]):
                if (sum(shells) - shells[-1]) + num == numbers:
                    shells.pop(-1)
                    shells.append(num)
                    break
            return shells

number_of_electrons = int(input())
print(distribution_func(number_of_electrons))