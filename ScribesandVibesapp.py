from tkinter import *
from MainScript import* 
from SpotifyAPI import *




root = Tk()
root.title("Scibes & Vibes")
root.geometry("640x640+0+0")
Heading = Label(root,text = 'Hows Your Day Going?' , font= ('arial' , 40,'bold'))
ent = Entry(root,width = 25)#.place(x = 200, y=200)
ent2 = Entry(root,width = 25)
ent.place(x = 200, y=200)
ent2.place(x = 200, y=350)
Heading.pack()



# print(JournalEntryString)
#entrybutton = Button(root,text = 'press the button when your journal antry is finished').place(x = 150,y=350)

def myclick():
    EntryScore = 0
    Entry = ent.get()
    EntryScore = ParseEntry(Entry)
    print(EntryScore)
def myclick2():
    Entry = ent.get()
    EntryScore = ParseEntry(Entry)
    print(EntryScore)


mutbut = Button(root,text = 'click me for inputing your journals', command = myclick)
mutbut2 = Button(root,text = 'click me for inputing your preferred artists', command = myclick2)
mutbut.pack()
mutbut2.pack()


root.mainloop()