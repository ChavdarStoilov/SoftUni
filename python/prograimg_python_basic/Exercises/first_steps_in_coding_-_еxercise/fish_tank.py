length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

capacity = length * width * height
capacity_letters = capacity / 1000
end_sum = capacity_letters * (1- percentage)
print(end_sum)