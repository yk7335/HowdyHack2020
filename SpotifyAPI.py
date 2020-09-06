import lyricsgenius
import random
from MainScript import* 

songList = []
songArtist = ["Drake", "Drake"]
genius = lyricsgenius.Genius("lhTCJEt_2R38qM9LC4b_TrPjurZL0Rwfljyp6J1C0IoLMG3le-MN0qbI94XSB70y")
songScoreList = []
songsStringList = []
TopThreeSongs = []

<<<<<<< HEAD
# def get_Artists():
#     while(len(songArtist) < 3):
#         artistname = str(input("Enter Artist: "))
#         songArtist.append(artistname)


def MakeSongList():
=======
def MakeSongList(songArtist):
>>>>>>> 1f7e42834b389a1f25a6e72d2dc98ff3deb3bba2
    for i in songArtist:
        artist = genius.search_artist(i, max_songs=50, sort="title")
        temp = random.randint(0,11)
        temp2 = 0
        while(temp2 < 10):
            if artist.songs[random.randint(0,11)] in songList:
                temp = random.randint(0,11) 
            else:
                songList.append(artist.songs[temp])
                temp = random.randint(0,11)
                temp2 += 1


def GetSongToString(SongTitle, SongArtist):
    song = genius.search_song(SongTitle, SongArtist)
    SongString = "".join(song.lyrics)
    return SongString



def GetSongScore():
<<<<<<< HEAD
    get_Artists()
    MakeSongList()
    for i in range (len(songsStringList)-1):
        songsStringList[i] = GetSongToString(str(songList[i].title), str(songList[i].artist))
=======
    MakeSongList(songArtist)
>>>>>>> 1f7e42834b389a1f25a6e72d2dc98ff3deb3bba2
    
    for i in range(49):
        songsStringList[i] = GetSongToString(str(songList[i].title), str(songList[i].artist))
    

    for i in range(49):
        songScoreList[i] =  ParseEntry(songsStringList[i])    
            
# the scores are in a song score list at the same index of thier lyrics and song title / artist
# to figure out which three we have to index through the list and see which has the highest score get
# index and see what song / artist is on that index in SongList