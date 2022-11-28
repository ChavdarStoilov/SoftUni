old_version = input().split(".")

if int(old_version[2]) < 9:
    old_version[2] = str(int(old_version[2]) +1)

else:
    old_version[2] = "0"

    if int(old_version[1]) < 9:
        old_version[1] = str(int(old_version[1]) + 1)

    else:
        old_version[1] = "0"
        old_version[0] = str(int(old_version[0]) + 1)

print(".".join(old_version))