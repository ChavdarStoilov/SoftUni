class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = []

        for song in args:
            self.songs.append(song)

    def add_song(self, song):

        if song.single:
            return f'Cannot add {song.name}. It\'s a single'

        elif self.published:
            return 'Cannot add songs. Album is published.'

        elif song in self.songs:
            return 'Song is already in the album.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'


    def remove_song(self, song_name: str):

        for song in self.songs:
            if song.name == song_name:
                if self.published:
                    return 'Cannot remove songs. Album is published.'
                return f'Removed song {song_name} from album {self.name}.'



        return 'Song is not in the album.'

    def publish(self):

        if self.published:
            return f'Album {self.name} is already published.'

        self.published = True
        return f'Album {self.name} has been published.'


    def details(self):

        songs = '\n'.join([f'== {the_song.get_info()}' for the_song in self.songs])

        return f'Album {self.name}\n{songs}'