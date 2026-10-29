import tkinter as me
from tkinter import messagebox
import sqlite3 



def convert_temp():

    cail_txt= cail_ent.get()
    fahren_txt=fahren_ent.get()






    try:
        if cail_txt:
            cail_value=float(cail_txt)
            fahren_rest=(cail_value*9/5)+32

            fahren_ent.delete(0,me.END)
            fahren_ent.insert(0,f"{fahren_rest:.2f}")

        elif fahren_txt:
            fahren_value=float(fahren_txt)
            cail_rest=(fahren_value-32)*5/9

            cail_ent.delete(0,me.END)
            cail_ent.insert(0,f"{cail_rest:.2f}")

        else:
            messagebox.showwarning("input Error","please enter a temprature in one of the fields.")


    except ValueError:
        messagebox("input error")


def clear_fields():



    cail_ent.delete(0,me.END)
    fahren_ent.delete(0,me.END)






cook=me.Tk()
cook.title("the tempreture app")
cook.geometry("500x500")






cail_lab=me.Label(cook,text="celsius")
cail_ent=me.Entry(cook,width=70)

fahren_lab=me.Label(cook,text="fahrenheit:")
fahren_ent=me.Entry(cook,width=70)





corv=me.Button(cook,text="convert",command=convert_temp)
clear=me.Button(cook,text="clear",command=clear_fields)


cail_lab.grid(row=0,column=0,padx=20,pady=20,sticky="w")
cail_ent.grid(row=0,column=1,padx=20,pady=20,)


fahren_lab.grid(row=1,column=0,padx=20,pady=20,sticky="w")
fahren_ent.grid(row=1,column=1,padx=20,pady=20)

corv.grid(row=2,column=0,columnspan=2,pady=10)
clear.grid(row=3,column=0,columnspan=2,pady=5)


cook.mainloop()