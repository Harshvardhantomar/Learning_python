def make_album(artist, album,songs=None):
    album = {'Artist':artist,'Album':album,}
    if(songs):
        album['Songs']=songs
    return album


print(make_album('Michael Jackson','Thriller'))
print(make_album('Michael Jackson','Bad',11))
print(make_album('The Weekend','Starboy',21))
