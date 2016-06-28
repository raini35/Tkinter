import Tkinter as tk 


LARGE_FONT=("Verdana", 12)

class SeaofBTCapp(tk.Tk):
	
	#args = any number of arguments 
	#kwargs = key word arguments 
	def __init__(self, *args, **kwargs): 
		
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self) 
		
		#Two ways to place items pack and grid
		container.pack(side="top", fill="both", expand=True)
		
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		
		#{} for dictionaries 
		self.frames = {}
		
		frame = StartPage(container, self)

		self.frames[StartPage] = frame 
		
		#sticky paramater is basically alignment (nsew = north south east west) 
		frame.grid(row=0, column=0, sticky="nsew")		
		
		self.show_frame(StartPage)
		
	def show_frame(self, cont): 
		
		frame = self.frames[cont]
		frame.tkraise() 
		
class StartPage(tk.Frame):
	
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10) #When you have 1 or 2 things to add to the window just use pack
		

app = SeaofBTCapp()
app.mainloop()