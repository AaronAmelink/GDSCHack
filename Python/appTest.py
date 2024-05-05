import tkinter as tk
from tkinter import ttk
from artManager import artManager
import time

#base set up 

root = tk.Tk()
root.geometry("500x400")
root.title("ArtVR")


def home_page():
    home_frame = tk.Frame(main_frame) #packs it into the mainframe

    lb = tk.Label(home_frame, text = 'Welcome to your Virtual Art Gallery!', font = ('Bold', 15))
    lb.pack()
    home_frame.pack(pady = 10)

def start_page():

    #set up for classes
    emptySpace = tk.Label(main_frame, text ="")
    emptySpace.pack(pady = 3)
    filterLabel =  tk.Label(main_frame, text = 'Display Filters', font = ('Bold',10))
    filterLabel.pack(pady = 5)
    """
    classification_list  = [
                    "Decorative art",
                    "Drawing", 
                    "Painting", 
                    "Photograph",
                    "Portfolio",
                    "Print",
                    "Sculpture",
                    "Technical material",
                    "Volume"]
    
    global class_value
    class_value = tk.StringVar(main_frame) #STRING THAT HOLDS THE CHOSEN CLASSIFICATION
    class_value.set("Classification")

    drop_Menu_Class = tk.OptionMenu(main_frame, class_value, *classification_list)
    drop_Menu_Class.config(width = 30)
    drop_Menu_Class.pack()"""

    #classification
    Nationality_list = [
            "American",
            "Austrian",
            "Belgian",
            "Bohemian",
            "British",
            "Canadian",
            "Chinese",
            "Czech",
            "Danish",
            "Dutch",
            "English",
            "Flemish",
            "French",
            "German",
            "Italian",
            "Japanese",
            "Mexican",
            "Netherlandish",
            "Norwegian",
            "Other",
            "Russian",
            "Scottish",
            "Spanish",
            "Swedish",
            "Swiss"]
    
    global national_value
    national_value = tk.StringVar(main_frame)
    national_value.set("Nationality")

    drop_Menu_Nat = tk.OptionMenu(main_frame, national_value, *Nationality_list)
    drop_Menu_Nat.config(width = 30)
    drop_Menu_Nat.pack()

    #classified editions
    edition_List = [
        "American Paintings, 1900-1945",
        "Dutch Paintings 17th Century",
        "French Paintings 15th-18th Centuries",
        "Italian Paintings 13th and 14th Centuries",
        "Italian Paintings 16th Century"
    ]

    global edition_value
    edition_value = tk.StringVar(main_frame)
    edition_value.set("Grouped Editions")

    drop_menu_edit = tk.OptionMenu(main_frame,edition_value, *edition_List)
    drop_menu_edit.config(width = 30)
    drop_menu_edit.pack()

 
    #number of pictures to display (Radio Buttons)
    global r
    r = tk.IntVar()
    emptySpace = tk.Label(main_frame, text ="")
    emptySpace.pack(pady = 3)
    numPic = tk.Label(main_frame, text = "Number of items to display")
    numPic.pack()
   
    tk.Radiobutton(main_frame, text = "30", variable=r, value = 30).pack()
    tk.Radiobutton(main_frame, text = "60", variable=r, value = 60).pack()
    tk.Radiobutton(main_frame, text = "90", variable=r, value = 90).pack()

    #page number
    emptySpace = tk.Label(main_frame, text ="")
    emptySpace.pack(pady = 2)
    pageNumLabel = tk.Label(main_frame, text = 'Enter page number of archive (1-100)')
    pageNumLabel.pack()

    global num
    num = tk.StringVar(main_frame)
    pageNum = tk.Entry(main_frame, textvariable =num)
    pageNum.pack()
    
    #load button
    load = tk.Button(main_frame, text = 'START', command = importPage)
    load.pack()


def hide_indicators():
    home_indicate.config(bg = '#c3c3c3')
    start_indicate.config(bg = '#c3c3c3')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg = 'black')
    delete_pages()
    page()

def importPage():
        
    am = artManager("testing")
    am.checkFilterMenuOn()
    time.sleep(3)
    am.getFilterTypes()
    am.toggleFilter("Images_online") #what is this for then
    time.sleep(10)
    am.getFilterTypes()
    time.sleep(10)
    #am.getArtSizingOff()
   
    if national_value.get() != "Nationality":
        am.toggleFilter(national_value.get())
        time.sleep(5)
    if edition_value.get() != "Grouped Editions":
        am.toggleFilter(edition_value.get())
        time.sleep(5)

    am.changeAmountOfArt(r.get())

    loop = int (num.get())
    for x in range (loop):
        am.goNextPage()
        time.sleep(5)
        

    
#gray bar on the left
option_frame = tk.Frame(root, bg='#c3c3c3')

#hoome button
home_button = tk.Button(root,text = 'Home', font = ('Bold', 15), fg = 'black', bd = 0, bg ='#c3c3c3', command =lambda: indicate(home_indicate, home_page))
home_button.place(x=20, y=50)

home_indicate = tk.Label(option_frame,text = '', bg = '#c3c3c3')
home_indicate.place(x = 3, y = 50, width = 5, height = 40)

#start button
start_button = tk.Button(root, text = 'Start',font = ('Bold', 15), fg = 'black', bd = 0, bg ='#c3c3c3', command = lambda: indicate(start_indicate, start_page))
start_button.place(x = 20, y = 100)

start_indicate = tk.Label(option_frame, text = '', bg = '#c3c3c3')
start_indicate.place(x = 3, y = 100, width = 5, height = 40)

option_frame.pack(side =tk.LEFT)
option_frame.configure(width=100, height =400)

#main white area
main_frame = tk.Frame(root, highlightbackground = 'black',highlightthickness = 2)
main_frame.pack(side=tk.TOP, fill = tk.BOTH, expand = True)
main_frame.configure(height= 400,width = 400)

root.mainloop()
