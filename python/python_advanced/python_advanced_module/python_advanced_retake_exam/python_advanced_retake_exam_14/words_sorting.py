def words_sorting(*args):
    dicti = {

    }

    for key in args:
        key_sum = [ord(s) for s in key]
        if key not in dicti:
            dicti[key] = 0
        dicti[key] = sum(key_sum)

    ordered_dicti = dicti

    if sum(dicti.values()) % 2 != 0:
        ordered_dicti = sorted(dicti.items(), key=lambda x: x[1], reverse=True)

    elif sum(dicti.values()) % 2 == 0:
        ordered_dicti = sorted(dicti.items(), key=lambda x: x[0])

    output = ''

    for items in ordered_dicti:
        item = items[0]
        values = items[1]

        output += f'{item} - {values}\n'

    return output

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
