from tkinter import*
top = Tk()
top.mainloop()

##pack() mrthod

from tkinter import  
parent = TK()
redbutton Button(parent, text="Red", fg = "red")
redbutton.pack(side = LEFT)
greenbutton = Button(parent, text="Black", fg = " black")
greenbutton.pack( stce = RIGHT)
bluebutton = Button(parent, Text", "lue")
bluebutton.pack(530_TOP_)
blackbutton = Button(parentest_Green, fg = "red")
blackbutton.pack(side = BOTTOM)
parent.sainloop()


## grid() method

from tkinter import*
parent = Tk()
name = Label(parent, fost "Name").grid(row = 0 , column = 0)
el= Entry(parent).grid(row = 0 , column = 1 )
password = Label(parent, text = "Password").grid(row = 1, column = 0)
e2 = Entry(parent).grid(row = 1 , column = 1)
submit Button(parent, text = "Submit").grid(row = 4, column = 0)
parent.mainloop()


## place () method 

from tkinter import*
top =Tk()
top.geometry("400x250")
name = Label(top, text= "Name").place(x = 30 , y = 50)
email = Label(top, text = " Email").place(X = 50, y = 90)
password= Label(top, Text ="Password").place(x=30,y=130)
e1 = Entry(top).place(x=80,y=50)
e2 = Entry(top).place( x= 80,y= 90)
e3 = Entry(top).place( x =95,y= 130)
top.mainloop()











