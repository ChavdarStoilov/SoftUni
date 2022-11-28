command = input()

companies = {}

while command != "End":
    company, employee = command.split(" -> ")

    if company not in companies:
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)

    command = input()

for name_company, employee_id in companies.items():
    print(name_company)
    for the_id in employee_id:
        print(f"-- {the_id}")