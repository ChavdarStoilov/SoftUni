period_for_check_patient = int(input())

doctors = 7

treated_patients = 0
untreated_patients = 0

for days in range(1, period_for_check_patient + 1):

    if days % 3 == 0:
        if treated_patients < untreated_patients:
            doctors += 1

    count_patient = int(input())

    if doctors < count_patient:
        untreated_patients += (count_patient - doctors)
        treated_patients += doctors
    elif doctors >= count_patient:
        treated_patients += count_patient



print(f"Treated patients: {treated_patients}.\n"
      f"Untreated patients: {untreated_patients}.")