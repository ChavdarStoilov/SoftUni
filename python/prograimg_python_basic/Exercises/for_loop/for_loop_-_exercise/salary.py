import sys

count_tabs_in_browser = int(input())
salary = int(input())

end_salary = salary

for sites in range(count_tabs_in_browser):
    site = str(input())
    if site == "Facebook":
        end_salary -= 150
    elif site == "Instagram":
        end_salary -= 100
    elif site == "Reddit":
        end_salary -= 50
    else:
        end_salary += 0

    if end_salary <= 0:
        print("You have lost your salary.")
        sys.exit(1)

print(end_salary)