import tkinter as tk 
from tkinter import ttk,messagebox
import sqlite3


def fake():
    con=sqlite3.connect("note_py.db")
    curs=con.cursor()
    curs.execute("""CREATE TABLE IF NOT EXISTS keeper (id INTEGER PRIMARY KEY,
    content TEXT)""")

    curs.execute("SELECT COUNT(*) FROM keeper")



    if curs.fetchone()[0]==0:
        curs.execute("INSERT INTO keeper (content)VALUES ('')")
        con.commit()
        con.close()


def save_db(text):
    try:
        con=sqlite3.connect("note_py.db")
        curs=con.cursor()
        curs.execute("UPDATE keeper SET content=? WHERE id=1",(text,))

        con.commit()
        con.close()
        messagebox.showinfo("Done","your note is save ")
    except Exception as e :
        messagebox.showerror("Error",f"note not saved.{e}")



def load():
    con=sqlite3.connect("note_py.db")
    curs=con.cursor()

    curs.execute("SELECT content FROM keeper WHERE id= 1")
    sat=curs.fetchone()
    con.close()
    return sat[0] if sat else ""



def note_book():

    fake()


    note=tk.Tk()
    note.title("my db notepad")
    note.geometry("500x500")

    book=ttk.Notebook(note)
    book.pack(pady=20,fill="both",expand=True)

    tab=ttk.Frame(book)
    book.add(tab,text="mi notes")


    labe = tk.Label(tab, text="the notes", font=("Calibri", 14))
    labe.pack(pady=5)

    no=tk.Text(tab,wrap="word",height=50,width=50,bg="brown",font=("calibri",16))
    no.pack(fill="both",expand=True)

    tex=load()
    no.insert("1.0",tex)


    btn=tk.Button(no, text="click to save to db",
                command=lambda: save_db((no.get("1.0",tk.END).strip())))
    btn.pack(pady=10,padx=10,side="bottom")


    tab1=ttk.Frame(book)
    book.add(tab1,text="settings")
    tk.Label(tab1,  text="settings (placeholder)").pack(pady=20)


    note.mainloop()

if __name__=="__main__":
    note_book()


