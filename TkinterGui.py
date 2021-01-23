from tkinter import*
from AzureAPI import*
from numpy import*
from SongAPI import*


base = Tk()
base.title("Scribes and Vibes") # header of the window
base.maxsize(1600,1600) # max width and height
base['bg'] = 'pink' # background color
passage = ""

def calcTextScoreInArray():
    result = []
    Message = MessageBox.get(1.0, "end-1c")
    client = authenticate_client()
    result = sentiment_analysis_example(client,Message, result)
    return result

def calcTextScore():
    result = []
    Message = MessageBox.get(1.0, "end-1c")
    client = authenticate_client()
    result = sentiment_analysis_example(client,Message, result)
    Response = "Positive={0:.2f}; Neutral={1:.2f}; Negative={2:.2f} \n".format(
        result[0],
        result[1],
        result[2],
    )
    Label(canvas, text = Response).grid(row = 1, column = 0, padx = 10, pady = 5)


def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:
        ele += "   "  
        str1 += ele   
    # return string   
    return str1  

ArtistName = []
def songArtistNames():
    name = Artist.get(1.0, "end-1c")
    ArtistName.append(name)
    Label(canvas, text = listToString((ArtistName))).grid(row = 4, column = 0, padx = 10, pady = 5)

def NumberOfSongs():
    number = Songs.get()
    Label(canvas, text = str(number)).grid(row = 6, column = 0, padx = 10, pady = 5)

#####trying to compare song score and passage score
def getSongrec():
    NumofSongs = Songs.get()
    result = []
    result = calcTextScoreInArray()
    songlist = getSongList(Artist.get(1.0, "end-1c"), int(NumofSongs))
    for j in range(int(NumofSongs)):
        Songscore = CalculateSongScore(songlist[j])
        if Songscore[0] == result[0]:
            Label(canvas, text = songlist[j]).grid(row = 8, column = 0, padx = 10, pady = 5)
            break
        elif Songscore[2] == result[2]:
            Label(canvas, text = songlist[j]).grid(row = 8, column = 0, padx = 10, pady = 5)
            break
        elif Songscore[0] <= result[0] + .2 or Songscore[0] >= result[0] - .2:
            Label(canvas, text = songlist[j]).grid(row = 8, column = 0, padx = 10, pady = 5)
            break
        elif Songscore[2] <= result[2] + .2 or Songscore[2] >= result[2] - .2:
            Label(canvas, text = songlist[j]).grid(row = 8, column = 0, padx = 10, pady = 5)
            break
        else:
            Label(canvas, text = songlist[len(songlist) - 1]).grid(row = 8, column = 0, padx = 10, pady = 5)
            break    

# creating the main gui
User_Interpahse_Frame = Frame(base, width = 600, height = 200, bg='pink')
User_Interpahse_Frame.grid(row = 0, column = 0, padx = 10, pady = 5)
#second layer of main Gui
canvas = Canvas(base, width=650, height = 380, bg='grey')
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)
# creating the main text box to enter the passage/how you feel
Label(User_Interpahse_Frame, text = "Write about how you are feeling and click sumbit for a song recomendation").grid(row = 0, column = 0)
MessageBox = Text(User_Interpahse_Frame, height = 10)
MessageBox.grid(row = 1, column = 0, padx = 5, pady = 5)
Button(User_Interpahse_Frame, text = "Submit Message", command = calcTextScore, bg = 'yellow').grid(row = 2, column = 0, padx = 5, pady = 5)
#creating song artist input
Label(User_Interpahse_Frame, text = "Write your favorite artist").grid(row = 3, column = 0)
Artist = Text(User_Interpahse_Frame, height = 2)
Artist.grid(row = 4, column = 0, padx = 5, pady = 5)
Button(User_Interpahse_Frame, text = "Submit Artist", command = songArtistNames, bg = 'yellow').grid(row = 5, column = 0, padx = 5, pady = 5)
#creating input of songs
Label(User_Interpahse_Frame, text = "Number of Songs (the more songs the more accurate the reading and also higher wait time)").grid(row = 6, column = 0)
Songs = Entry(User_Interpahse_Frame)
Songs.grid(row = 7, column = 0, padx = 5, pady = 5)
Button(User_Interpahse_Frame, text = "Enter number of songs", command = NumberOfSongs, bg = 'yellow').grid(row = 8, column = 0, padx = 5, pady = 5)
#creating where the results will be outputted
Label(canvas, text = "Passage Score:").grid(row = 0, column = 0, padx = 10, pady = 3)
Label(canvas, text = "Prefered Artist:").grid(row = 3, column = 0, padx = 10, pady = 5)
Label(canvas, text = "Number of Songs:").grid(row = 5, column = 0, padx = 10, pady = 5)
#Final label to get answer
Button(canvas, text = "Get Song Recommendation!", command = getSongrec, bg = "Yellow").grid(row = 7,column = 0, padx = 10, pady = 5)


base.mainloop()
