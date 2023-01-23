from tkinter import *
import requests
import json

# from datetime import datetime

# window Initialize
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Weather app")

# main app


def showWeather():
    # api key from OpenWeatherMap
    api_key = "5f69e8d5987522fd23c3360b5a1e37ce"
    # city name from user
    city_name = city_value.get()
    # Api Url
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
        city_name + '&appid='+api_key + '&units=metric' + '&lang=pl'

    response = requests.get(api_url)

    weather_info = response.json()

    text_box.delete("1.0", 'end')

    if weather_info["cod"] == 200:
        temp = int(weather_info["main"]["temp"])
        feels_like = int(weather_info['main']['feels_like'])
        pressure = weather_info["main"]['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed']
        clouds = weather_info['weather'][0]['description']

        weather = f'Pogoda dla {city_name}\nTemperatura:{temp}\u00B0C\nTemperatura odczuwalna:{feels_like}\u00B0C\nCisnienie:{pressure} hPa\nWilgotnosc:{humidity}%\nPredkosc wiatru:{wind_speed} m/s\nPogoda: {clouds}'

        text_box.insert(INSERT, weather)

    else:
        text_box.insert(INSERT, f'No data')


# fronted
city_head = Label(root, text="Enter the city name",
                  font="Arial 12 bold").pack(pady=10)

# lang = StringVar()

# language1 = Radiobutton(root, text="English",
#                         variable=lang, value='en').place(x=60, y=30)
# language2 = Radiobutton(root, text="Polish", variable=lang,
#                         value='pl', command=showWeather).place(x=140, y=30)
# language3 = Radiobutton(root, text="German", variable=lang,
#                         value='de').place(x=220, y=30)


city_value = StringVar()

inp_city = Entry(root, textvariable=city_value, width=24,
                 font="Arial 14 bold").pack(padx=100, pady=10)


check = Button(root, text="Check the weather", font="Arial 12 bold",
               bg="lightblue", fg="black", width=20, command=showWeather).pack(pady=30)

weather_now = Label(root, text="The actual weather:",
                    font="Arial 12 bold").pack(pady=10)

text_box = Text(root, width=46, height=8)
text_box.pack()


root.mainloop()
