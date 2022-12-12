command = str(input())


while command != "Welcome!":
    name_of_students = command

    if name_of_students == "Voldemort":
        print("You must not speak of that name!")
        break

    chr_of_names = len(name_of_students)

    if chr_of_names < 5:
        print(f"{name_of_students} goes to Gryffindor.")
    elif chr_of_names == 5:
        print(f"{name_of_students} goes to Slytherin.")
    elif chr_of_names == 6:
        print(f"{name_of_students} goes to Ravenclaw.")
    elif chr_of_names > 6:
        print(f"{name_of_students} goes to Hufflepuff.")

    command = str(input())

else:
    print("Welcome to Hogwarts.")