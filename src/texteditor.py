from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(1.0, END)  # Исправлено с 0.0 на 1.0 для Python 3
    
def saveFile():
    global filename
    if filename == "Untitled" or filename is None:  # Если файл новый
        saveAs()
        return
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:  # Добавлена кодировка
            f.write(text.get(1.0, END))
    except:
        showerror(title="Oops!", message="Unable to save file...")

def saveAs():
    global filename
    f = asksaveasfilename(defaultextension='.txt')  # Используем asksaveasfilename вместо asksaveasfile
    if not f:  # Если пользователь отменил
        return
    
    filename = f  # Сохраняем новое имя файла
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text.get(1.0, END))
    except:
        showerror(title="Oops!", message="Unable to save file...")

def openFile():
    global filename
    f = askopenfilename()  # Используем askopenfilename вместо askopenfile
    if not f:  # Если пользователь отменил
        return
    
    try:
        with open(f, 'r', encoding='utf-8') as file:
            text.delete(1.0, END)
            text.insert(1.0, file.read())
        filename = f  # Сохраняем имя открытого файла
    except:
        showerror(title="Oops!", message="Unable to open file...")

root = Tk()
root.title("Python text editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
