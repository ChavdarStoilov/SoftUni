usernames_number = int(input())

unique_usernames = set()

for _ in range(usernames_number):

    username = input()
    unique_usernames.add(username)


print('\n'.join(unique_usernames))