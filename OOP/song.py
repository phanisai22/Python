class Song:

    def __init__(self, title, artist, duration=0):
        self.name = title
        self.artist = artist
        self.duration = duration


class Album:

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("various artist")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.tracks)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Only applicable to the second approach of load data function
            in which the Artist object calls the add_song() function .

            this method adds the song to the album in the collection
            a new album is created in the collection if it does't really exists ."""

        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name+" not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album "+name)

        album_found.add_song(title)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return field
        else:
            return None


# def load_data():
#     new_artist = None
#     new_album = None
#     artist_list = []
#
#     with open('albums.txt', 'r') as albums:
#         for line in albums:
#             # data row should consist of
#             # (artist_field, album_field, year_field, song_field)
#             # separated with tabs.
#             artist_field, album_field, year_field, song_field = \
#                 tuple(line.strip('\n').split('\t'))
#             year_field = int(year_field)
#             # print(artist_field, ":", album_field, ":",
#             #  year_field, ":", song_field)
#
#             if new_artist is None:
#                 new_artist = Artist(artist_field)
#                 artist_list.append(new_artist)
#             elif new_artist.name != artist_field:
#                 # we have just read the details of a new artist.
#                 # retrieve the artist object if there is one,
#                 #  otherwise create a new artist object
#                 # and add it to the artist list
#                 new_artist = find_object(artist_field, artist_list)
#                 if new_artist is None:
#                     new_artist = Artist(artist_field)
#                     artist_list.append(new_artist)
#                 new_album = None
#
#             if new_album is None:
#                 new_album = Album(album_field, year_field, new_artist)
#                 new_artist.add_album(new_album)
#             elif new_album.name != album_field:
#                 # we have just read a new album for the current artist.
#                 # Retrieve the album object if there is one.
#                 # otherwise create a new album object
#                 # and add it to the corresponding artist's album's list.
#                 new_album = find_object(album_field, new_artist.albums)
#                 if new_album is None:
#                     new_album = Album(album_field, year_field, new_artist)
#                     new_artist.add_album(new_album)
#
#             # create a new song object.
#             new_song = Song(song_field, new_artist)
#             new_album.add_song(new_song)
#
#             # after read the last line of the text file, we will have an artist and
#             # album that haven't been store - process them now.
#         # if new_artist is not None:
#         #     if new_album is not None:
#         #         new_artist.add_album(new_album)
#         #         artist_list.append(new_artist)
#
#         return artist_list

# Another way to implement this load data function using oops concept .

def load_data():

    artist_list = []
    with open('albums.txt', 'r') as albums:

        for line in albums:
            # data row should consist of
            # (artist_field, album_field, year_field, song_field)
            # separated with tabs.
            artist_field, album_field, year_field, song_field = \
                tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            # print(artist_field, ":", album_field, ":",
            #  year_field, ":", song_field)

            new_artist = find_object(artist_field, artist_list)

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    with open('checkfile.txt', 'w') as checkfile:
        for artist in artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    print('{}\t{}\t{}\t{}'.
                          format(artist.name, album.name, album.year, song.name),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(load_data())))
    create_checkfile(load_data())
