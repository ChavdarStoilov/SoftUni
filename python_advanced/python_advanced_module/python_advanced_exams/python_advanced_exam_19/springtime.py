def start_spring(**kwargs):
    spring = {}

    for type, objects in kwargs.items():
        if objects not in spring.keys():
            spring[objects] = []
        spring[objects].append(type)


    sorted_elements = sorted(spring.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for element in sorted_elements:
        type_name = element[0]
        obj = sorted(element[1])
        list_obj = '\n-'.join(obj)
        result.append(f'{type_name}:\n-{list_obj}')

    return '\n'.join(result)

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))



