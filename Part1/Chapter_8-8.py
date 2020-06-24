#Album

def make_album(artist_name, album_title, track=''):
    album = {'Artist_Name':artist_name,'Album_title':album_title,'Album_Track':track}
    if track:
        album['track']=track
    return album


while True:
    album_name = input('put your album name :')
    if album_name=='quit':
        break
    album_title = input('put your album title :')
    if album_title=='quit':
        break
    print(make_album(album_name, album_title))