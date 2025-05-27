from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(1.0, END) 
    
def saveFile():
    global filename
    if filename == "Untitled" or filename is None:  
        saveAs()
        return
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:  
            f.write(text.get(1.0, END))
    except:
        showerror(title="Oops!", message="Unable to save file...")

def saveAs():
    global filename
    f = asksaveasfilename(defaultextension='.txt') 
    if not f: 
        return
    
    filename = f  
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text.get(1.0, END))
    except:
        showerror(title="Oops!", message="Unable to save file...")

def openFile():
    global filename
    f = askopenfilename() 
    if not f: 
        return
    
    try:
        with open(f, 'r', encoding='utf-8') as file:
            text.delete(1.0, END)
            text.insert(1.0, file.read())
        filename = f  
    except:
        showerror(title="Oops!", message="Unable to open file...")

def changeSelectedTextColor(color):
    try:
        if text.tag_ranges(SEL):
            sel_start = text.index(SEL_FIRST)
            sel_end = text.index(SEL_LAST)
            text.tag_add("colored", sel_start, sel_end)
            text.tag_config("colored", foreground=color)
    except:
        pass 

root = Tk()
root.title("Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400, fg="black")
text.pack()

menubar = Menu(root)

# Меню File
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

# Меню Сolor для изменения цвета выделенного текста
colormenu = Menu(menubar)
colormenu.add_command(label="Black", command=lambda: changeSelectedTextColor("black"))
colormenu.add_command(label="Red", command=lambda: changeSelectedTextColor("red"))
colormenu.add_command(label="Blue", command=lambda: changeSelectedTextColor("blue"))
colormenu.add_command(label="Green", command=lambda: changeSelectedTextColor("green"))
menubar.add_cascade(label="Color", menu=colormenu)

root.config(menu=menubar)
root.mainloop()
