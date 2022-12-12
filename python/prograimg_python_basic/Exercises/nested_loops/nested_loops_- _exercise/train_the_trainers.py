count_of_number_jury = int(input())
name_of_presentation = str(input())

avg = 0
final_assessment = 0
final_assessments =0

while name_of_presentation != "Finish":
    for rating in range(1, count_of_number_jury +1):
        rate = float(input())
        avg += rate
        final_assessment += rate
        final_assessments += 1

    print(f"{name_of_presentation} - {avg / count_of_number_jury:.2f}.")
    avg = 0
    name_of_presentation = str(input())


print(f"Student's final assessment is {final_assessment / final_assessments:.2f}.")