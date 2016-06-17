from Tkinter import * 

root = Tk()

def printName(event): 
	print("Chello my name is Bucky!")
	
button_1 = Button(root, text="Print my name")
button_1.bind("<Button-2>", printName)
button_1.pack()

root.mainloop()


