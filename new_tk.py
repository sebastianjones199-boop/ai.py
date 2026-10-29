# import tkinter as tk
# from tkinter import filedialog
# # root=tk.Tk()
# # root.title("MY TKINTER APP")
# def on_key_press(event):
#     print(f"key pressed: {event.char}")


# root=tk.Tk()
# entry=tk.Entry(root)
# entry.pack()
# entry.bind("<Key>", on_key_press)

# name=tk.StringVar()
# name.set("john doe")

# lab=tk.Label(root,textvariable=name)
# lab.pack()

# ent=tk.Entry(root,textvariable=name)
# ent.pack()

# def upd_name():
#     name.set("jane smith")

# but=tk.Button(root,text="change name",command=upd_name)
# but.pack(padx=20,pady=20)

# root.withdraw()

# def show():
#     messagebox.showinfo("info","this is an information massage.")

# def ask():
#     response=messagebox.askyesno("qustion","do you like tkinter")
#     print(f"user response:{response}")

# show()
# ask()

# root.withdraw()

# def open():
#     file=filedialog.askopenfilename(
#         title="openafile",
#         filetypes=(("Text file","*.txt"),("All file","*.*"))

#     )

#     if file:
#         print(f"selected file {file}")


# open()



# import tkinter as tk

# class myapp:
#     def __init__(self, master):
#         self.master = master
#         master.title("simple app")
#         self.label=tk.Label(master,text="hello,world")
#         self.label.pack(pady=10)
#         self.greet=tk.Button(master,text="greet", command=self.greet)
#         self.greet.pack()
#         self.close=tk.Button(master,text="close",command=master.quit)
#         self.close.pack()
#     def greet(self):
#         self.label.config(text="greeting")

# if __name__=="__main__":
#     root=tk.Tk()
#     app=myapp(root)
#     root.mainloop()

import tkinter as tk
from tkinter import filedialog
dubem=tk.Tk()
dubem.title("MY NOTE BOOK APP")
dubem.geometry("100x100")
jef=tk.Label(dubem,text="hello world")
jef.pack(padx=20,pady=20)
def key (event):
    print(f"key preesd{event}")
det=tk.Button(text="clike button",command="clike me")
det.pack()
fun=tk.Text()
fun.pack()



dubem.mainloop()












# root.destroy()










# root.mainloop()