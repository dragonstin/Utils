from  Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

def buttonClick():
    print 'function'


root = Tk()

topFrame = Frame(root)
bottomFrame = Frame(root)

myEntry = Entry(topFrame)

myEntry.text= tkFileDialog.askdirectory()


label = Label(topFrame, text="Diretory:")
myButton = Button(topFrame, text="Search files to rename", fg="blue", command=buttonClick)


topFrame.grid(row=0)
bottomFrame.grid(row=5)
label.grid(row=1, sticky=E)
myEntry.grid(row=1, column=1)
myButton.grid(row=1, column=2)

root.mainloop()