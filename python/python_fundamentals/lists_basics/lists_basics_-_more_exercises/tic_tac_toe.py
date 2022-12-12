first_line = input().split()
second_line = input().split()
third_line = input().split()

tabel = [first_line, second_line, third_line]

first_win = False
second_win = False

if first_line[0] == "2" and second_line[0] == "2" and third_line[0] == "2" or \
        first_line[1] == "2" and second_line[1] == "2" and third_line[1] == "2" or \
        first_line[2] == "2" and second_line[2] == "2" and third_line[2] == "2":
        second_win = True

elif first_line.count("2") == 3 or \
        second_line.count("2")== 3 or \
        third_line.count("2") == 3:
        second_win = True

elif first_line[0] == "2" and second_line[1] == "2" and third_line[2] == "2" or \
        first_line[2] =="2" and second_line[1] == "2" and third_line[0] == "2":
        second_win = True

if first_line[0] == "1" and second_line[0] == "1" and third_line[0] == "1" or \
        first_line[1] == "1" and second_line[1] == "1" and third_line[1] == "1" or \
        first_line[2] == "1" and second_line[2] == "1" and third_line[2] == "1":
        first_win = True


elif first_line.count("1") == 3 or \
        second_line.count("1")== 3 or \
        third_line.count("1") == 3:
        first_win = True


elif first_line[0] == "1" and second_line[1] == "1" and third_line[2] == "1" or \
        first_line[2] =="1" and second_line[1] == "1" and third_line[0] == "1":
        first_win = True

if first_win:
    print("First player won")
elif second_win:
    print("Second player won")
else:
    print("Draw!")