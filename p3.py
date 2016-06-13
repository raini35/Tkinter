from Tkinter import * 

root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
#fill=X means that it fill the widget as wide as the parent
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
#fill=Y means that it fill the widget as high as the parent
three.pack(side=LEFT, fill=Y)

root.mainloop()