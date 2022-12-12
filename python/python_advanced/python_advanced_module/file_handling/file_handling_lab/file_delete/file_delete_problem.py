import os

if os.path.exists(r'C:\CVStoilov\python\SoftUni\pythob_advanced\file_handling\file_handling_lab\file_writer\my_first_file.txt'):
    os.remove(r'C:\CVStoilov\python\SoftUni\pythob_advanced\file_handling\file_handling_lab\file_writer\my_first_file.txt')

else:
    print('File already deleted!')