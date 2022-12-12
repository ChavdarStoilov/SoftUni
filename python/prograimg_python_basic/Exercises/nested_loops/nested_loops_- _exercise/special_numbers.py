some_numer = int(input())

for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                if some_numer % first == 0 and some_numer % second == 0 and some_numer % third == 0 and some_numer % fourth ==0:
                    print(f"{first}{second}{third}{fourth}", end=" ")
