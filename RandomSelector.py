import random
from Tkinter import*


#Pick random quote
def randomPick():
    return random.choice(masterList)


#Make window call for each button mash
def Call(text):
    text.delete(1.0,END)
    text.insert(1.0,randomPick())



#Open text file and store each quote lab = Label(root, text=randomPick())as element of a list
masterList = open('file.txt').read().split('\n\n')

#Make a background window of specified attributes
root = Tk()
root.title("Random Quote Selector")
root.geometry("750x100")

#Create frame for button
topFrame = Frame(root)
topFrame.pack(side=TOP)

#Create text object and fill with random quote
txt = Text(root, width=200, height=10, )
txt.pack()
txt.insert(1.0, randomPick())

#Define and create button.  Use lambda
button = Button(topFrame, text="Quote", command=lambda: Call(txt))
button.pack()

#Execute main loop
root.mainloop()




