def make_album(artist, album):
    album = {'Artist':artist.title(),'Album':album.title()}
    return album


while True:
    print("Tell me about your favorite album")
    print("Enter 'q' at any time to quit")
    artist_name = input('Artist Name:')
    if(artist_name == 'q'):
        break
    album_name = input("Album's Name:")
    if(album_name=='q'):
        break

    print(f"{make_album(artist_name,album_name)}\n")




