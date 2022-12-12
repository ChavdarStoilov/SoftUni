def open_file(file_name):

    try:
        with open(file_name, 'r') as file:
            print(file.readlines())
        print('File found')
    except:
        print('File not found')


open_file('text.txt')