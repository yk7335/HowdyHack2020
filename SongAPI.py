
import lyricsgenius
import numpy as np
from AzureAPI import*

def getSongList(artist, numberofSongs):
    genius = lyricsgenius.Genius("lhTCJEt_2R38qM9LC4b_TrPjurZL0Rwfljyp6J1C0IoLMG3le-MN0qbI94XSB70y")
    artist = genius.search_artist(artist, max_songs=numberofSongs, sort="popularity", include_features=False)
    songlist = []
    songlist = artist.songs
    return songlist


def CalculateSongScore(Song):
    genius = lyricsgenius.Genius("lhTCJEt_2R38qM9LC4b_TrPjurZL0Rwfljyp6J1C0IoLMG3le-MN0qbI94XSB70y")
    INDsongScore = []
    Lyrics = Song.lyrics
    client = authenticate_client()
        
    try:
        INDsongScore = sentiment_analysis_example(client, Lyrics, INDsongScore)
    except:
        Lyrics = Lyrics[:5115]
        INDsongScore = sentiment_analysis_example(client, Lyrics, INDsongScore)

    return INDsongScore

