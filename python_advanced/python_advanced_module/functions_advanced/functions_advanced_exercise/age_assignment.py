def age_assignment(*args, **kwargs):
    sorted_names = sorted(args)
    result = []

    for name in sorted_names:
        for key, value in kwargs.items():
            if name.startswith(key):
                result.append(f"{name} is {value} years old.")


    return '\n'.join(result)

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))