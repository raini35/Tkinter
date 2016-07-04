#6.3.16 Part 7 
#		Part 8 - for windows download numpy & pandas
#		Part 9

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation 
#from matplotlib import style -> I need the newer versiom of matplot lib to use this

import Tkinter as tk 
import ttk

import urllib
import json

#import pandas as pd 
import numpy as np

LARGE_FONT=("Verdana", 12)
#style.use("ggplot") -> I need the newer verison of matplotlib to use this 

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
	dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000' 
	#data = urllib.request.urlopen(dataLink)
	#data = data.readall().decode("utf-8")
	data = urllib.urlopen(dataLink).read()
	data = json.loads(data)
	data = data["btc_usd"]
	data = pd.DataFrame(data)
	
	buys = data[(data['type']=="bid")]
	buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
	buyDates = (buys["datestamp"]).tolist()
		
	sells = data[(data['type']=="ask")]
	sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
	sellDates = (sells["datestamp"]).tolist()
	
	a.clear()
	
	a.plot_date(buyDates, buys["price"])
	a.plot_date(sellDates, sells["price"])
	
	
	
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
		for F in (StartPage, BTCe_page): 
			
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
		
		label = tk.Label(self, text=
	""" ALPHA Bitcoin trading application
use at your own risk. There is no promise
of warranty.""", font=LARGE_FONT)

		label.pack(pady=10, padx=10) #When you have 1 or 2 things to add to the window just use pack
		
		#lambda creates a temporary variable so that you can pass arguments for functions 
		#that you use for command (See below)
		button1 = ttk.Button(self, text="Agree", 
							command=lambda: controller.show_frame(BTCe_page))
		button1.pack()
		
		button2 = ttk.Button(self, text="Disagree", command=quit)
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
		

class BTCe_page(tk.Frame): 
	
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = ttk.Button(self, text="Back to Home", 
							command=lambda: controller.show_frame(StartPage))
		button1.pack()
		
	
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
		
		
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
		
	
		
app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()