import Tkinter as tk 
import ttk


LARGE_FONT=("Verdana", 12)

class SeaofBTCapp(tk.Tk):
	
	#args = any number of arguments 
	#kwargs = key word arguments 
	def __init__(self, *args, **kwargs): 
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		#self.tk.call('wm', 'iconbitmap', "/Users/rfg40/Documents/client.x")
		#self.iconbitmap(default='client.ico')		
		self.tk.call('wm', 'iconbitmap', self, 'client.xbm')
		
		container = tk.Frame(self) 
		#Two ways to place items pack and grid
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		
		#{} for dictionaries 
		self.frames = {}
		
		#this lets you go through the different pages
		for F in (StartPage, PageOne, PageTwo): 
			
			frame = F(container, self)

			self.frames[F] = frame 
		
			#sticky paramater is basically alignment (nsew = north south east west) 
			frame.grid(row=0, column=0, sticky="nsew")		
		
		self.show_frame(StartPage)
		
	def show_frame(self, cont): 
		
		frame = self.frames[cont]
		frame.tkraise() 
		
def qf(param):
	print(param)
	
class StartPage(tk.Frame):
	
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10) #When you have 1 or 2 things to add to the window just use pack
		
		#lambda creates a temporary variable so that you can pass arguments for functions 
		#that you use for command (See below)
		button1 = ttk.Button(self, text="Visit Page1", 
							command=lambda: controller.show_frame(PageOne))
		button1.pack()
		
		button2 = ttk.Button(self, text="Visit Page2", 
							command=lambda: controller.show_frame(PageTwo))
		button2.pack()

class PageOne(tk.Frame): 
	
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = ttk.Button(self, text="Back to Home", 
							command=lambda: controller.show_frame(StartPage))
		button1.pack()
		
		button2 = ttk.Button(self, text="Page Two", 
							command=lambda: controller.show_frame(PageTwo))
		button2.pack()
		
		
class PageTwo(tk.Frame): 
	
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = ttk.Button(self, text="Back to Home", 
							command=lambda: controller.show_frame(StartPage))
		button1.pack()
		
		button2 = ttk.Button(self, text="Page One", 
							command=lambda: controller.show_frame(PageOne))
		button2.pack()

		
app = SeaofBTCapp()
app.mainloop()