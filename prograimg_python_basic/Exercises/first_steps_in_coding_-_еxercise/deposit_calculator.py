deposit = float(input())
term = int(input())
percentage_interest = float(input()) / 100

all = deposit * percentage_interest
interest = all / 12
end_sum = deposit + term * interest
print(end_sum)