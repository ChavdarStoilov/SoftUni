some_string = str(input()).split()
count_of_shuffle = int(input())




for shuffle in range(count_of_shuffle):
    end_list = []
    center_of_the_string = len(some_string) // 2
    left_side_of_string = some_string[0:center_of_the_string]
    right_side_of_string = some_string[center_of_the_string::]
    for word in range(len(left_side_of_string)):
        end_list.append(left_side_of_string[word])
        end_list.append(right_side_of_string[word])

    some_string = end_list

print(some_string)
