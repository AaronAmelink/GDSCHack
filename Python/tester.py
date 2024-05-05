import tkinter as tk
from tkinter import ttk

# Create object 
root = tk.Tk() 
  
# Adjust size 
root.geometry( "200x200" ) 
  
# Change the label text 
def show(): 
    label.config( text = clicked.get() ) 
  
# Dropdown menu options 
options = [ 
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
] 
  
# datatype of menu text 
clicked = tk.StringVar() 
  
# initial menu text 
clicked.set( "Monday" ) 
  
# Create Dropdown menu 
drop = tk.OptionMenu( root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text 
button = tk.Button( root , text = "click Me" , command = show ).pack() 
  
# Create Label 
label = tk.Label( root , text = " " ) 
label.pack() 
  
# Execute tkinter 
root.mainloop() 