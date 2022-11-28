def calculations(first_number, second_number, type_of_operation):

    result_of_calculation = 0

    if type_of_operation == "multiply":
        result_of_calculation = first_number * second_number
    elif type_of_operation == "divide":
        result_of_calculation = int(first_number / second_number)
    elif type_of_operation == "add":
        result_of_calculation = first_number + second_number
    elif type_of_operation == "subtract":
        result_of_calculation = first_number - second_number

    return result_of_calculation

type_of_operation = str(input())
first_number = int(input())
second_number = int(input())
print(calculations(first_number, second_number, type_of_operation))

