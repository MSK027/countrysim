# MK V0.0.2 10/06/22
from tkinter import *
from PIL import Image, ImageTk



print ("Welcome to Simon's Autism Simulator")

""" class city:
    def __init__(self, name, node, extractor, stockpile, consumption, manpower, modifier, 
                edicts, provincemod, countrymodifier, factories):
        self.name = name
        self.factories = factories
        self.node = node
        self.extractor = extractor
        self.stockpile = stockpile
"""



# Object that works the value modifications in the economy tab. MORE RESEARCH NECESSARY
class econMods:
    def __init__(self, city, key, val):
        self.city = city
        self.key = key
        self.val = val

        city[key] = val

class colonize:
    def __init__(self, playerNation, city):
        self.city = city
        self.playerNation = playerNation

        playerNation.append[city]


# Dictionary list to fill for each city. Work for Simon. The Key is the unchanging part like 'coalStock' and the value like how much coal is in there.
# Template City = ['actuallyFillThisInFirst : Value']
York = ['Key : Value', 'Key2 : Value2']
Cambridge = ['Key : Value', 'Key2 : Value2', 'Key3 : Value3']


# List of dictionary lists for each faction
playerNation = [York, Cambridge]


## tk window and headers
main = Tk()
main.title("Country Sim 1800s")
main.geometry("1920x1080")
lbl = Label(main, text="Main Menu")

#Load background
mainback = Image.open("mainback1.jpg")
picture = ImageTk.PhotoImage(mainback)
mnbck = Label(main, image=picture)

#Buttons
new = Button(main, text="New Game")
load = Button(main, text="Load Game")
options = Button(main, text="Options")
exit = Button(main, text="Exit Game")

#Arrange and run
lbl.pack()
mnbck.pack()
new.pack()
load.pack()
options.pack()
exit.pack() 
main.mainloop()
