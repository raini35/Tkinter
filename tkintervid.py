import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import Tkinter as tk 
import ttk


LARGE_FONT=("Verdana", 12)

class SeaofBTCapp(tk.Tk):
	
	#args = any number of arguments 
	#kwargs = key word arguments 
	def __init__(self, *args, **kwargs): 
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		#self.tk.call('wm', 'iconbitmap', self, 'client.xbm')
		
		tk.Tk.wm_title(self, "Sea of BTC Client")
		
		container = tk.Frame(self) 
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		
		#{} for dictionaries 
		self.frames = {}
		
		#this lets you go through the different pages
		for F in (StartPage, PageOne, PageTwo, PageThree): 
			
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
		
		button3 = ttk.Button(self, text="Graph Page", 
							command=lambda: controller.show_frame(PageThree))
		button3.pack()

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
		label = tk.Label(self, text="Page Two", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = ttk.Button(self, text="Back to Home", 
							command=lambda: controller.show_frame(StartPage))
		button1.pack()
		
		button2 = ttk.Button(self, text="Page One", 
							command=lambda: controller.show_frame(PageOne))
		button2.pack()

class PageThree(tk.Frame): 
	
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = ttk.Button(self, text="Back to Home", 
							command=lambda: controller.show_frame(StartPage))
		button1.pack()
		
		f = Figure(figsize=(5,5), dpi=100)
		a = f.add_subplot(111)
		a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,4,5,3,4])
	
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
			
	
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
		
app = SeaofBTCapp()
app.mainloop()