to_do_notes = input().split("-")

to_do_list = [] * 10

while to_do_notes[0] != "End":

    to_do = "".join(to_do_notes)

    to_do_list.append(to_do)

    to_do_notes = input().split("-")

to_do_list.sort()
end_list = []
end_value = ""
for char in to_do_list:

    if char[:2] == "10":
        end_value = (char[2:])
    else:
        end_list.append(char[1:])

if end_value == "":
    print(end_list)
else:
    end_list.append(end_value)
    print(end_list)