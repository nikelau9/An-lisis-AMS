from tkinter import Tk, StringVar,Y, W, X, PhotoImage, Toplevel, YES, END, Label,ANCHOR, ACTIVE, RIGHT,LEFT, Button, BOTH, TOP, BOTTOM, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL, Checkbutton, Listbox, MULTIPLE
import pandas as pd



root = Tk()
root.config(bg='white')
root.geometry('200x50')
root.minsize(width=200, height=50)
root.title('AMS CNA')


def abrirI():
    a = Confirmar()
    if a==False:
        return None
    else:
        import programaejemplodatos.py

def abrirU():
    a = Confirmar()
    if a==False:
        return None
    else:
        import programaejemplodatos.py

def Confirmar():
    resultado = messagebox.askokcancel("", "Confirmar selección")
    if resultado == True:
        return True
    else:
        return False



botonbat = Button(root, text= '^{129}I', bg='green2', command= abrirI).pack()
botonbi = Button(root, text= '^{236}U', bg='blue', command= abrirU).pack()
root.mainloop()
