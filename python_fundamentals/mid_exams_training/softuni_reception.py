def reception(first_employee, second_employee, third_employee, count):

    needed_hours = 0

    while count > 0:
        count -= first_employee + second_employee + third_employee
        needed_hours += 1
        if needed_hours % 4 == 0:
            needed_hours +=1




    return f"Time needed: {needed_hours}h."


first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())

print(reception(first_employee_efficiency, second_employee_efficiency, third_employee_efficiency, student_count))
