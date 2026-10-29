from tkinter.filedialog import*
import tkinter as tk
import sqlite3
def init_db():
    con= sqlite3.connect("my notepad app.db")
    cursor=con.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS notes
                   id INTEGER, 
                   title TEXT UNIQUE,
                   content TEXT NOT NULL
                   """)
    con.commit()
    
def savefile():
    fin = asksaveasfile(mode = "w",filetypes=[('text file','.txt')])
    if fin is None:
        return
    text=str (ent.get('END'))
    fin.write(text)
    fin.close()



def openfile():
    fix = askopenfiles(mode='r',filetypes=[('text file','*.')])
    if fix is not None:
        con=fix.read()
        ent.insert("INSERT",con)


def clearfile():
    ent.delete(1.0,'END')




dude=tk.Tk()

dude.geometry("400x600")

dude.title("my notepad app")

dude.config(bg="blue")

jet=tk.Frame(dude)
jet.pack(padx=5,pady=6,anchor="nw")

ac=tk.Button(dude,text="open it",bg="red",command=openfile)
ac.pack(in_= jet,side= "left")


a3=tk.Button(dude,text="save",bg="pink",command=savefile)
a3.pack(in_= jet , side="left")

a2=tk.Button(dude,text="side",bg="pink",command=clearfile)
a2.pack(in_= jet , side="left")

a1=tk.Button(dude,text="close",bg="pink",command=exit)
a1.pack(in_= jet , side="left")

ent=tk.Text(dude,wrap="word", bg= "#A4F9E45B",font=("Arial",15))
ent.pack(padx=10,pady=4,expand=True,fill="both")
dude.mainloop()