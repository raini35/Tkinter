#Learned how to make a menu, & drop down menus :O :O :O 

from Tkinter import * 


def doNothing(): 
	print("ok ok I won't...")
		
root = Tk() 

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

root.mainloop() 