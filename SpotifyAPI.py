import lyricsgenius
import random
from MainScript import* 

songArtist = ["Drake"]
songList=[]

genius = lyricsgenius.Genius("lhTCJEt_2R38qM9LC4b_TrPjurZL0Rwfljyp6J1C0IoLMG3le-MN0qbI94XSB70y")

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

print(songList[0].artist)
#song = genius.search_song(str(songList[0]), str(songList[0][1]))

# test = song.lyrics.split(" ")
# for i in test:o
#     print(i, " "0)



