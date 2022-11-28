employees_happiness = list(map(int, input().split()))
factor = int(input())

result = [happy * factor for happy in employees_happiness]

avg_happiness = sum(result) / len(result)

end_result = list(filter(lambda x: x >= avg_happiness, result))

if len(end_result) >= len(result) / 2:
    print(f"Score: {len(end_result)}/{len(result)}. Employees are happy!")
else:
    print(f"Score: {len(end_result)}/{len(result)}. Employees are not happy!")