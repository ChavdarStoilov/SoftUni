def add_songs(*args):

    songs = {

    }

    for info in args:
        title_song = info[0]
        lyrics = info[1]

        if title_song not in songs:
            songs[title_song] = []
        songs[title_song].extend(lyrics)


    output = ''
    for i, x in songs.items():
        output += f'- {i}\n'

        if '\n'.join(x) != '':
            a = '\n'.join(x)
            output += f'{a}\n'

    return output

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))


