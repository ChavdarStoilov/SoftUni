import os

def create_file(file):

    if os.path.exists(file):
        with open(file, 'w') as empty:
            empty.writable()
            empty.close()
    else:
        with open(file, 'w') as new_file:
            new_file.writable()
            new_file.close()

def add_into_file(file, content):

    if not os.path.exists(file):
        with open(file, 'w') as new_file:
            new_file.write(f'{content}\n')
            new_file.close()
    else:
        with open(file, 'a+') as add_content:
            add_content.write(f'{content}\n')
            add_content.close()


def replace_into_file(file, old_string, new_string):
    new_content = ''

    if not os.path.exists(file):
        print('An error occurred')
    else:
        with open(file, 'r') as replacer:
            line = replacer.readlines()
            for words in line:
                if old_string in words:
                    words = words.replace(old_string, new_string)

                new_content += words
            replacer.close()

        with open(file, 'w') as replace_old:
            replace_old.write(new_content)
            replace_old.close()

def delete_file(file):

    if not os.path.exists(file):
        print('An error occurred')
    else:
        os.remove(file)



while True:

    command = input().split('-')

    if command[0] == 'End':
        break

    if command[0] == 'Create':
        create_file(command[1])
    elif command[0] == 'Add':
        add_into_file(command[1], command[2])
    elif command[0] == 'Replace':
        replace_into_file(command[1], command[2], command[3])
    elif command[0] == 'Delete':
        delete_file(command[1])