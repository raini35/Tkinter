from Tkinter import * 


class RainiersButtons: 
	#master = root = main window
	def __init__(self, master):
		frame = Frame(master)
		frame.pack() 
		
		self.printButton = Button(frame, text="Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)
		
		#frame.quit is equivalent to breaking the mainloop
		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)
			
	def printMessage(self):
		print("Wow, this actually worked!")
		
root = Tk()
b=RainiersButtons(root)
c=RainiersButtons(root)
root.mainloop()