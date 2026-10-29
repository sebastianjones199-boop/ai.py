# import sqlite3
# fit=sqlite3.connect("jef.db")

# f=fit.cursor()
# # f.execute(""" CREATE TABLE fun (name TEXT,
# #           city TEXT,
# #           location TEXT)""")


# jet=[('james','lagos','iba'),('justin','anambara','awka')]

# f.executemany(" INSERT INTO FUN VALUES(?,?,?)",jet)
# fit.commit()




# try:
#     with open("fun file tnt","w") as file:
#          file.write("\n")
#          file.write("\n")
#          file.write("\n")
#          file.write("\n")
#          file.write("\n")

# except FileExistsError:
#      print("file not found")

# for i in range(100):
#     print(i)

# jef=-2
# while jef <=1:
#     print(jef)
#     jef-1
import tkinter as tk
dubem=tk.Tk()
dubem.geometry("500x500")
dubem.title("my firs app")
dect=tk.Label(dubem,text="welcome to my app",font=('Araril',16))
dect.pack(padx=20,pady=20)
fill=tk.Text(dubem,height=2,font=('arial',28))
fill.pack(padx=10,pady=10)
mrt=tk.Entry(dubem)
mrt.pack(padx=23,pady=23)
press=tk.Button(dubem,text="press me",font=('Arail',12))
press.pack(padx=12,pady=12)
jeff=tk.Frame(dubem)
jeff.columnconfigure(0,weight=1)
jeff.columnconfigure(1,weight=1)
jeff.columnconfigure(2,weight=1)
jeff.columnconfigure(3,weight=1)
jeff.columnconfigure(4,weight=1)

erick=tk.Button(jeff,text="1" font=('Arial',18))
erick.grid(row=0,column=0,sticky=tk.W+tk.E)
erick.grid(row=0,column=0,sticky=tk.W+tk.E)
erick.grid(row=0,column=0,sticky=tk.W+tk.E)
erick.grid(row=0,column=0,sticky=tk.W+tk.E)
erick.grid(row=0,column=0,sticky=tk.W+tk.E)
erick.grid(row=0,column=0,sticky=tk.W+tk.E)




dubem.mainloop()