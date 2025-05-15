from tkinter import *

from tkinter import ttk

import requests

def data_get():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=baea916f4db7806aad0ee0565178ddd9").json()
    w_label.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Wscube Tech")
win.config(bg = "blue")
win.geometry("570x570")


name_label = Label(win, text="Wscube Weather App", font=("Time New Roman",20,"bold"))
name_label.place(x=50, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="Indian States",values=list_name , font=("Time New Roman",15,"bold"), textvariable=city_name)
com.place(x=50, y=120, height=50, width=450)


w_label = Label(win, text="weather Climet", font=("Time New Roman",10))
w_label.place(x=50, y=260, height=50, width=200)

w_label = Label(win, text="", font=("Time New Roman",10))
w_label.place(x=300, y=260, height=50, width=200)

wb_label = Label(win, text="weather Description", font=("Time New Roman",10))
wb_label.place(x=50, y=330, height=50, width=200)

wb_label1 = Label(win, text="", font=("Time New Roman",10))
wb_label1.place(x=300, y=330, height=50, width=200)

temp_label = Label(win, text="Temprature", font=("Time New Roman",10))
temp_label.place(x=50, y=400, height=50, width=200)

temp_label1 = Label(win, text="", font=("Time New Roman",10))
temp_label1.place(x=300, y=400, height=50, width=200)

per_label = Label(win, text="Pressure", font=("Time New Roman",10))
per_label.place(x=50, y=470, height=50, width=200)

per_label1 = Label(win, text="", font=("Time New Roman",10))
per_label1.place(x=300, y=470, height=50, width=200)


done_button = Button(win, text="Done", font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190, height=50, width=100, x=230)


win.mainloop()