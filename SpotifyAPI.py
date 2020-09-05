import lyricsgenius
genius = lyricsgenius.Genius("lhTCJEt_2R38qM9LC4b_TrPjurZL0Rwfljyp6J1C0IoLMG3le-MN0qbI94XSB70y")
artist = genius.search_artist("Drake", max_songs=10, sort="title")
print(artist.songs)
