some_text = input()

list_of_chars = tuple(ch for ch in some_text)

end_result  = {}

for char in list_of_chars:

    if char not in end_result.keys():
        end_result[char] = list_of_chars.count(char)



for chars in sorted(end_result):

    print(f'{chars}: {end_result[chars]} time/s')
