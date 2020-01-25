from Tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


label = Label(topFrame, text="Diretory:")
myButton = Button(topFrame, text="Button 1", fg="blue")
myEntry = Entry(root)

label.grid()

myButton.pack()


root.mainloop()