from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city=city_name.get()
  
    url = ""
    data = requests.get(url).json()

    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=(data["main"]["pressure"]))

# city_name = "Gujarat"
# print(data)

win = Tk()
win.title("My Weather Report")
win.config(bg="blue")
win.geometry("500x570")

name_label = Label(win,text="Python Weather App",font=("Times New Roman",30 ,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name = [
    "Delhi", "Mumbai", "Ahmedabad", "Chennai", "Kolkata", "Jaipur", "Lucknow", "Patna", "Bhopal"
]  # ✅ Use cities instead of states

com = ttk.Combobox(win,text="Python Weather App", values=list_name ,font=("Times New Roman",20 ,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_label = Label(win,text="Weather Climate",font=("Times New Roman",18 ))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text=" ",font=("Times New Roman",18 ))
w_label1.place(x=250,y=260,height=50,width=210)


wd_label = Label(win,text="Weather Description",font=("Times New Roman",18 ))
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1 = Label(win,text=" ",font=("Times New Roman",18 ))
wd_label1.place(x=250,y=330,height=50,width=210)


temp_label = Label(win,text="Temperature",font=("Times New Roman",18 ))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text=" ",font=("Times New Roman",18 ))
temp_label1.place(x=250,y=400,height=50,width=210)


per_label = Label(win,text="Pressure",font=("Times New Roman",18 ))
per_label.place(x=25,y=470,height=50,width=210)
per_label1 = Label(win,text=" ",font=("Times New Roman",18 ))
per_label1.place(x=250,y=470,height=50,width=210)


done_button = Button(win,text="Done!!!",font=("Times New Roman",20 ,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)


win.mainloop()
