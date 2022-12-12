import re


def barcode(the_barcode):

    end_result = ""

    pattern = r"\b((?<=!)[A-Z][a-z]{3,})(!:)([[])([[:alpha:]]{8,}|[\w ]+)\b"

    regex = re.finditer(pattern, the_barcode)

    reg_num = [bar.group("barcode") for bar in regex]

    if len(reg_num) != 0:
        for number in reg_num[0]:
            if number.isdigit():
                end_result += number
    else:
        return "Invalid barcode"

    if end_result == "":
        return "Product group: 00"
    else:
        return f"Product group: {end_result}"

number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    some_barcodes = input()
    print(barcode(some_barcodes))