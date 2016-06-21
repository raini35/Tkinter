#Learned how to make a menu, & drop down menus :O :O :O 
#Learned how to make a tool bar
from Tkinter import * 


def doNothing(): 
	print("ok ok I won't...")
		
root = Tk() 

######## MAIN MENU ########

#every time you make something in Tkinter you must declare a variable
drop_down_menu = Menu(root) 
root.config(menu=drop_down_menu)

subMenu=Menu(drop_down_menu)
drop_down_menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Now Project...", command=doNothing) 
subMenu.add_command(label="Now...", command=doNothing) 
subMenu.add_separator() 
subMenu.add_command(label="Exit", command=doNothing) 

subMenu_Edit=Menu(drop_down_menu) 
drop_down_menu.add_cascade(label="Edit", menu=subMenu_Edit) 
subMenu_Edit.add_command(label="Redo", command=doNothing)

######## TOOLBAR #######

toolbar = Frame(root, bg="grey")

button_1 = Button(toolbar, text="Insert Image", command=doNothing) 
button_1.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)
root.mainloop() 