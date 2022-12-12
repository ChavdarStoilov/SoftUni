some_sting = input().split(", ")
substring = input().split(", ")

end_result = []

for char in some_sting:
    for char_two in substring:
        if char in char_two and not char in end_result:
            end_result.append(char)
            break

print(end_result)
