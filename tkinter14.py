#Placing pictures in Tkinter
#So Python 2.7 Can only work with gifs or ppms(?)
from Tkinter import *

root = Tk() 

photo = PhotoImage(file='Sideshowbob3.gif') 
label = Label(root, image=photo)
label.pack() 

root.mainloop()