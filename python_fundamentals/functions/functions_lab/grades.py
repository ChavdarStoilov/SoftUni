def grades(grade):
    result_of_grade = ""

    if 2.00 <= grade <= 2.99:
        result_of_grade = "Fail"
    elif 3.00 <= grade <= 3.49:
        result_of_grade = "Poor"
    elif 3.50 <= grade <= 4.49:
        result_of_grade = "Good"
    elif 4.50 <= grade <= 5.49:
        result_of_grade = "Very Good"
    elif 5.50 <= grade <= 6.00:
        result_of_grade = "Excellent"

    return result_of_grade

number_grade = float(input())
print(grades(number_grade))