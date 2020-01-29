import os 
from  Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.directory = tkFileDialog.askdirectory()

path = root.directory 

files_in_dir = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(path.replace('/','\\')):
   folder = r.replace(' ', '_')
   print('renaming... ' + r + ' to '+ folder)
   os.rename(r, folder)

   for item in f:
      file = os.path.join(folder, item)
      fileNewName =  file.replace(' ', '_')
      print('renaming... ' + file + ' to '+ fileNewName)
      
      files_in_dir.append(fileNewName)  
      
      os.rename(file,fileNewName)
  