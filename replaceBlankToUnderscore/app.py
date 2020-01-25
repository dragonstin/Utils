from Tkinter import *

root = Tk()

def buttonClick():
    print(myEntry.get())

topFrame = Frame(root)

bottomFrame = Frame(root)

label = Label(topFrame, text="Diretory:")
myButton = Button(topFrame, text="Button 1", fg="blue", command=buttonClick)
myEntry = Entry(topFrame)

topFrame.grid(row=0)
bottomFrame.grid(row=5)
label.grid(row=1, sticky=E)
myEntry.grid(row=1, column=1)
myButton.grid(row=1, column=2)

root.mainloop()