# MK V0.0.2 10/06/22
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


print ("Welcome to CountrySim")


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



def menu(root):

    ## tk page and headers
    page = tk.Frame(root)
    page.grid()
    resx = root.winfo_screenwidth()
    resy = root.winfo_screenheight()
    root.geometry(str(resx) + "x" + str(resy))
    lbl = Label(page, text="Main Menu")


    #Load background
    menuback = Image.open("menuback1.jpg")
    picture = ImageTk.PhotoImage(menuback)
#    menu.configure(background=menuback)
    mnbck = Label(page, image=picture)

    #Buttons
    new = Button(page, text="New Game")
    load = Button(page, text="Load Game")
    options = Button(page, text="Options")
    exit = Button(page, text="Exit Game", command=root.destroy)

    #Arrange and run
    lbl.pack()
    mnbck.pack()
    new.place(x = resx*.45, y = resy * .25)
    load.place(x = resx*.45, y = resy * .30)
    options.place(x = resx*.45, y = resy * .35)
    exit.place(x = resx*.45, y = resy * .40) 
    

def switch():
    for widget in root.winfo_children():
        widget.destroy()
    

root = Tk()
root.title("Country Sim Victorian")
menu(root)
root.mainloop()


""" class city:
    def __init__(self, name, node, extractor, stockpile, consumption, manpower, modifier, 
                edicts, provincemod, countrymodifier, factories):
        self.name = name
        self.factories = factories
        self.node = node
        self.extractor = extractor
        self.stockpile = stockpile
"""