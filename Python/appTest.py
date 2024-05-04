import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("500x400")
root.title("ArtVR")

def home_page():
    home_frame = tk.Frame(main_frame) #packs it into the mainframe
    lb = tk.Label(home_frame, text = 'welcome! r ya ready', font = ('Bold', 30))
    lb.pack()
    home_frame.pack(pady = 10)

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def start_page():

    start_frame = tk.Frame(main_frame)
    lb = tk.Label(start_frame, text = 'start!')
    lb.pack()
    start_frame.pack(pady = 10)


    #dropdown boxes
        #classification
    classification_list  = [
                    "Decorative art (177)",
                    "Drawing (24700)", 
                    "Painting (2557)", 
                    "Photograph (1787)",
                    "Portfolio (38)",
                    "Print(25009)",
                    "Sculpture (3358)",
                    "Technical material (37)",
                    "Volume (439)"]
    
    class_value = tk.StringVar(root)
    class_value.set("Classification")

    drop_Menu_Class = tk.OptionMenu(root, class_value, *classification_list)
    drop_Menu_Class.pack()

        #classification
    Nationality_list = [
            "American (23980)",
            "Austrian (229)",
            "Belgian (43)",
            "Bohemian (274)",
            "British (2795)",
            "Canadian (15)",
            "Chinese (10)",
            "Czech (31)",
            "Danish (22)",
            "Dutch (2675)",
            "English (447)",
            "Flemish (1446)",
            "French (13865)",
            "German (5259)",
            "Italian (6385)",
            "Japanese (4)",
            "Mexican (5)",
            "Netherlandish (1064)",
            "Norwegian (4)",
            "Other (1155)",
            "Russian (37)",
            "Scottish (129)",
            "Spanish (284)",
            "Swedish (108)",
            "Swiss (518)"]
    
    national_value = tk.StringVar(root)
    national_value.set("Nationality")

    drop_Menu_Nat = tk.OptionMenu(root, national_value, *Nationality_list)
    drop_Menu_Nat.pack()

        #classified editions
    edition_List = [
        "American Paintings, 1900–1945 (19)",
        "Dutch Paintings 17th Century (142)",
        "French Paintings 15th–18th Centuries (22)",
        "Italian Paintings 13th and 14th Centuries (65)",
        "Italian Paintings 16th Century (35)"
    ]

    edition_value = tk.StringVar(root)
    edition_value.set("Grouped Editions")

    drop_menu_edit = tk.OptionMenu(root,edition_value, *edition_List)
    drop_menu_edit.pack()

    #number of pictures to display
    r = tk.IntVar()
   
    tk.Radiobutton(root, text = "30", variable=r, value = 1).pack()
    tk.Radiobutton(root, text = "60", variable=r, value = 2).pack()
    tk.Radiobutton(root, text = "90", variable=r, value = 3).pack()

def hide_indicators():
    home_indicate.config(bg = '#c3c3c3')
    start_indicate.config(bg = '#c3c3c3')


def indicate(lb, page):
    hide_indicators()
    lb.config(bg = 'black')
    delete_pages()
    page()

#########the basic structure of this app follows a youtube video - rmbmr to change it so its not plagirism


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
main_frame.pack(side=tk.LEFT)
main_frame.configure(height= 400,width = 400)

root.mainloop()