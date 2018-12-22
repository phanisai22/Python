import pickle

# album = ('ed shereen',
#          '2018',
#          ((1, 'sick boy'),
#           (2, 'shape of you'),
#           (3, 'flower market')))
#
# with open("album.pickle", "wb") as albumFile:
#     pickle.dump(album, albumFile)

# with open("album.pickle", "rb") as readAlbumFile:
#     albumRead = pickle.load(readAlbumFile)
#
# print(albumRead)
#
# artist, year, track = albumRead
#
# print("{} \n {} \n {}".format(artist, year, track))
#___________________________________________________________________________

# album = ('ed shereen',
#          '2018',
#          ((1, 'sick boy'),
#           (2, 'shape of you'),
#           (3, 'flower market')))
#
# even = list(range(0, 20, 2))
# odd = list(range(1, 20, 2))
#
# with open("album.pickle", "wb") as albumFile:
#     pickle.dump(album, albumFile)
#     pickle.dump(even, albumFile)
#     pickle.dump(odd, albumFile)
#
# with open('album.pickle', 'rb') as readAlbum:
#     tempAlbum = pickle.load(readAlbum)
#     readEven = pickle.load(readAlbum)
#     readOdd = pickle.load(readAlbum)
#
# print(tempAlbum, readEven, readOdd)


# pickle.loads(b"cos\nsystem\n(S'rm album.pickle'\ntR.")
#this fucking deletes the file man.