import os 
from  Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.directory = tkFileDialog.askdirectory()
print (root.directory)

path = root.directory 

os.path.isdir(path)

files_in_dir = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(path):
   for item in f:
      files_in_dir.append(os.path.join(r, item))
    #  os.rename(os.path.join(r, item), os.path.join(r, item).replace(' ', '_'))
   os.rename(r, r.replace(' ', '_'))


for item in files_in_dir:
   newName = item
   os.rename(item, newName.replace(' ', '_'))
   print("file in dir: ", item)
