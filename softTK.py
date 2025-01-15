from tkinter import*
top = Tk()
top.mainloop()

##pack() mrthod

from tkinter import *
parent = Tk()
redbutton = Button(parent, text="Red", fg="red")
redbutton.pack(side=LEFT)
greenbutton = Button(parent, text="Green", fg="green")
greenbutton.pack(side=RIGHT)
bluebutton = Button(parent, text="Blue", fg="blue")
bluebutton.pack(side=TOP)
blackbutton = Button(parent, text="Black", fg="black")
blackbutton.pack(side=BOTTOM)
parent.mainloop()


## grid() method

from tkinter import *
parent = Tk()
name = Label(parent, text="Name").grid(row=0, column=0)
e1 = Entry(parent).grid(row=0, column=1)
password = Label(parent, text="Password").grid(row=1, column=0)
e2 = Entry(parent).grid(row=1, column=1)
submit = Button(parent, text="Submit").grid(row=4, column=0)
parent.mainloop()

## place () method 

from tkinter import *
top = Tk()
top.geometry("400x250")

name = Label(top, text="Name").place(x=30, y=50)
email = Label(top, text="Email").place(x=30, y=90)  #
password = Label(top, text="Password").place(x=30, y=130)  

e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
e3 = Entry(top).place(x=80, y=130)  
top.mainloop()









