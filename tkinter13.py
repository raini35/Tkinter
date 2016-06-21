#Learned about canvas and graphics 
from Tkinter import * 

root = Tk() 

canvas  = Canvas(root, width=200, height=100) 
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red") 

#The first two arguments are the coordinates for the top left point of the shape
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

#It's good to delete shapes to make dynamic pages
canvas.delete(redLine)
#canvas.delete(blackLine)
#canvas.delete(greenBox)
canvas.delete(ALL)
root.mainloop()