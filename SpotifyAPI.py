import lyricsgenius
import random
from MainScript import* 

songList = []
songArtist = []
genius = lyricsgenius.Genius("lhTCJEt_2R38qM9LC4b_TrPjurZL0Rwfljyp6J1C0IoLMG3le-MN0qbI94XSB70y")

def get_Artists():
    while(len(songArtist) < 3):
        artistname = str(input("Enter Artist: "))
        songArtist.append(artistname)


def MakeSongList():
    for i in songArtist:
        artist = genius.search_artist(i, max_songs=15, sort="title")
        temp = random.randint(0,11)
        temp2 = 0
        while(temp2 < 10):
            if artist.songs[random.randint(0,11)] in songList:
                temp = random.randint(0,11) 
            else:
                songList.append(artist.songs[temp])
                temp = random.randint(0,11)
                temp2 += 1

get_Artists()
#song = genius.search_song("Marvins Room", str(songList[0].artist))
MakeSongList()

def GetSongToString(SongTitle, SongArtist):
    song = genius.search_song(SongTitle, SongArtist)
    SongString = "".join(song.lyrics)
    return SongString

for i in range(5):
    temp3 = GetSongToString(str(songList[i].title), str(songList[i].artist))
    print(temp3)
    print("----------------------------------------------------------------")
