tail = str(input())
body = str(input())
head = str(input())

the_list = [tail,body,head]

the_list[0],the_list[2] = the_list[2],the_list[0]

print(the_list)


# the_list.append(third_string)
# the_list.append(second_string)
# the_list.append(first_string)
#
# print(the_list)