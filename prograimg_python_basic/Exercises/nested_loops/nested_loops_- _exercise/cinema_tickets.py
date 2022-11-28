first_input = input()

total_tickets = 0
students_tickets = 0
standard_tickets = 0
kit_tickets = 0

while first_input != "Finish":
    movie = first_input
    capacity = int(input())

    count_current_movie = 0
    second_input = input()

    while second_input != "End":
        type_ticket = second_input

        if type_ticket == "student":
            students_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        else:
            kit_tickets += 1

        total_tickets += 1
        count_current_movie += 1
        if count_current_movie == capacity:
            break

        second_input = input()
    percentage = (count_current_movie / capacity) * 100
    print(f"{movie} - {percentage:.2f}% full.")


    first_input = input()

percentage_students_tickets = (students_tickets / total_tickets) * 100
percentage_standard_tickets = (standard_tickets / total_tickets) * 100
percentage_kit_tickets = (kit_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}\n"
    f"{percentage_students_tickets:.2f}% student tickets.\n"
    f"{percentage_standard_tickets:.2f}% standard tickets.\n"
    f"{percentage_kit_tickets:.2f}% kids tickets.")





######## My first code:
# name_of_movie = input()
# free_seats = int(input())
#
# students_tickets = 0
# standard_tickets = 0
# kit_tickets = 0
# tickets_for_movie = 0
# all_tickets = 0
#
# finished = False
#
# while name_of_movie != "Finish":
#     type_ticket = input()
#     while type_ticket != "End":
#         if type_ticket == "student":
#             students_tickets += 1
#         elif type_ticket == "standard":
#             standard_tickets += 1
#         else:
#             kit_tickets += 1
#
#         all_tickets += 1
#         tickets_for_movie += 1
#         type_ticket = input()
#
#         if type_ticket == "Finish":
#             finished = True
#             break
#
#     percentage = (tickets_for_movie / free_seats) * 100
#     print(f"{name_of_movie} - {percentage:.2f}% full.")
#     tickets_for_movie = 0
#
#
#
#     if finished:
#         break
#
#     name_of_movie = input()
#     free_seats = int(input())
#
# total_tickets = standard_tickets + students_tickets + kit_tickets
# percentage_students_tickets = (students_tickets / total_tickets) * 100
# percentage_standard_tickets = (standard_tickets / total_tickets) * 100
# percentage_kit_tickets = (kit_tickets / total_tickets) * 100
#
# print(f"Total tickets: {total_tickets}\n"
#     f"{percentage_students_tickets:.2f}% student tickets.\n"
#     f"{percentage_standard_tickets:.2f}% standard tickets.\n"
#     f"{percentage_kit_tickets:.2f}% kids tickets.")