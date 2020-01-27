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
      if '.txt'or '.docx' in item:
         files_in_dir.append(os.path.join(r, item))

for item in files_in_dir:
   print("file in dir: ", item.replace(' ', '_'))