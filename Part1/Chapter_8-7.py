#Album

def make_album(artist_name, album_title, track=''):
    album = {'Artist_Name':artist_name,'Album_title':album_title,'Album_Track':track}
    if track:
        album['track']=track
    return album

album1 = make_album('chu','song',3)
print(album1)
album1 = make_album('chu','song')
print(album1)

print(make_album('chu','song',3))
print(make_album('lee','love'))