import tkinter as fo
from time import strftime
import pyttsx3
from zoneinfo import ZoneInfo
from datetime import datetime


voice=pyttsx3.init()

stopwatch_time=0

alarm_time=""

alarm_running=False

stopwatch_running=False

jezz=fo.Tk()


lab=fo.Label(jezz,font=("Times New Roman",40),bg="red",fg="brown")

stopwatch_lab=fo.Label(jezz,font=("Times New Roman",30),
                       bg="black",fg="white")

stopwatch_lab.pack()  



world_lab=fo.Label(jezz,font=("Times New Roman",20),
                   bg="black",fg="white")
world_lab.pack(pady=10)




lab.pack(padx=30)


def update_item():
    current_time=strftime("%H:%M:%S")
    lab.config(text=current_time)
    jezz.after(1000,update_item)

def set_alarm():
    global alarm_time
    alarm_time=alarm_entry.get()


def check_alarm():
    global alarm_running
    current_time=strftime("%H:%M:%S")

    if current_time == alarm_time:
        alarm_running=True

    if alarm_running:
        voice.say("Alarm! Wake up!")
        voice.runAndWait()

    jezz.after(1000,check_alarm)


def stop_alarm():
    global alarm_running
    alarm_running=False









alarm_entry=fo.Entry(jezz)
alarm_entry.pack(pady=5)



alarm_button=fo.Button(jezz,text="SET ALARM",command=set_alarm)
alarm_button.pack(pady=5)



alarm_stop=fo.Button(jezz,text="STOP ALARM",command=stop_alarm)
alarm_stop.pack(pady=5)









def world_time():
   
    lagos=datetime.now(ZoneInfo("Africa/Lagos"))
    london=datetime.now(ZoneInfo("Europe/London"))
    tokyo=datetime.now(ZoneInfo("Asia/Tokyo"))

    
    text="Lagos: "+lagos.strftime("%H:%M:%S")
    text+="\nLondon: "+london.strftime("%H:%M:%S")
    text+="\ntokyo:  "+tokyo.strftime("%H:%M:%S")


    world_lab.config(text=text)
    jezz.after(1000,world_time)








def speak_time():
    current_time=strftime("%H:%M:%S")
    voice.say("welcome perfect the time is"+current_time)
    voice.runAndWait()








update_item()


def update_stopwatch():
    global  stopwatch_time

    if stopwatch_running:
        stopwatch_time+=1
        stopwatch_lab.config(text=stopwatch_time)
        jezz.after(1000,update_stopwatch)





def start_stopwatch():
    global stopwatch_running
    stopwatch_running=True
    update_stopwatch()
    



def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False
    
    
    
buttons=fo.Frame(jezz)
buttons.pack(pady=10)







def reset_stopwatch():
    global stopwatch_time
    stopwatch_time=0
    stopwatch_lab.config(text=stopwatch_time)
    





star=fo.Button(buttons,text="START",command=start_stopwatch)
star.pack(padx=5)

stop=fo.Button(buttons,text="STOP",command=stop_stopwatch)
stop.pack(padx=5,)


reset=fo.Button(buttons,bg="red",fg="white",    text="RESET",command=reset_stopwatch)
reset.pack(pady=5)



spaek=fo.Button(jezz,text="tell me the time",command=speak_time)
spaek.pack(pady=5)



def change_mode(color):
    jezz.config(bg=color)






fo.Button(jezz,text="color_one",
          command=lambda:change_mode("pink")).pack(padx=5)



fo.Button(jezz,text="color_two",
          command=lambda:change_mode("orange")).pack(padx=5
          )


jezz.config(bg="blue")


check_alarm()

world_time()
jezz.mainloop()






    
    
