import os

def write_report(message):

    with open('report.txt', 'a+') as report:
        report.write(message)
        report.close()

def end_result(result):
    report = ''
    for ext in result:
        the_ext = ext[0]
        list_file = ext[1]
        report += f'.{the_ext}\n'
        for name in list_file:
            report += f'- - - {name}.{the_ext}\n'

    write_report(report)

sorted_list = {}
list_files = os.listdir()

for file in list_files:
    name, extension = file.split('.')

    if extension not in sorted_list.keys():
        sorted_list[extension] = [name]
    else:
        sorted_list[extension].append(name)

result = sorted(sorted_list.items(), key=lambda x: (x[0], x[1]))

end_result(result)
