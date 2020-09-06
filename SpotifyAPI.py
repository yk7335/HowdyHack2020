import lyricsgenius
import random
from MainScript import* 

songList = []
songArtist = ["Drake", "Drake"]
genius = lyricsgenius.Genius("lhTCJEt_2R38qM9LC4b_TrPjurZL0Rwfljyp6J1C0IoLMG3le-MN0qbI94XSB70y")
songScoreList = []
songsStringList = []
TopThreeSongs = []

def MakeSongList(songArtist):
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
    MakeSongList(songArtist)
    
    for i in range(49):
        songsStringList[i] = GetSongToString(str(songList[i].title), str(songList[i].artist))
    

    for i in range(49):
        songScoreList[i] =  ParseEntry(songsStringList[i])    
            
# the scores are in a song score list at the same index of thier lyrics and song title / artist
# to figure out which three we have to index through the list and see which has the highest score get
# index and see what song / artist is on that index in SongList