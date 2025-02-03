# подключаем библиотеку для работы с запросами
import requests
from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("Погода")
root.geometry("400x400")

def getTemperature(city):
	url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_var.get() + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
	weather_data = requests.get(url).json()
	temperature = round(weather_data['main']['temp'])
	return temperature

def selected(event):
    # получаем выделенный элемент
    selection = combobox.get()
    city_var.set(selection)
    label["text"] = f"Температура: {getTemperature(city_var.get())}"
    print(selection)

city = ["Москва", "Курск", "Курчатов", "Владивосток"]
label = ttk.Label(borderwidth=2, relief="solid", padding=8)
label.pack(anchor=CENTER, fill=X, padx=5, pady=5)

city_var = StringVar(value = city[0])
label["text"] = f"Температура: {getTemperature(city_var.get())}"
combobox = ttk.Combobox(textvariable = city_var, values = city, state = "readonly")
combobox.pack(anchor=CENTER, padx=6, pady=6)

#temperature_feels = round(weather_data['main']['feels_like'])
combobox.bind("<<ComboboxSelected>>", selected)
 
root.mainloop()