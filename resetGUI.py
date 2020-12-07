import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as mb
import os

def reset():
  if os.path.exists("AppData\personal.ini"):
    os.remove("AppData\personal.ini")
    mb.showinfo(title="Done", message="Patched !")
  else:
    mb.showerror(title="RWI already reseted !", message="Please launch RWI at least one time else it won't work !")

root = Tk()

root.geometry('800x500')
root.configure(background='#F0F8FF')
root.title('RWI RESETER')

Label(root, text='RWI RESETER', bg='#F0F8FF', font=('courier', 48, 'bold')).place(x=168, y=44)

Label(root, text='This will reset RWI editor , including trial days , ONLY WORKING WITH PORTABLE VERSION', bg='#F0F8FF', font=('helvetica', 12, 'bold')).place(x=38, y=101)

Button(root, text='RESET', bg='#FF0000', font=('courier', 48, 'italic'), command=reset).place(x=247, y=180)


root.mainloop()
