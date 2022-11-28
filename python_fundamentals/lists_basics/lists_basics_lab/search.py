the_number_of_lines = int(input())
the_word = str(input())

list_of_the_string = []
filter_string = []

for lines in range(the_number_of_lines):
    string = str(input())
    list_of_the_string.append(string)

    if the_word in string:
        filter_string.append(string)


print(list_of_the_string)
print(filter_string)

