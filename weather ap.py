import tkinter as tk
import requests

root = tk.Tk()
root.title("Weather App")
root.geometry("500x600")

entry = tk.Entry(root, width=30, font=("Arial", 16))
entry.pack(pady=20)

def get_weather():
    city = entry.get()
    api_key = "bcec37e941ce4b1785c172208260301"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        label_city.config(text=f"City: {city}")
        label_temp.config(text=f"Temperature: {temp} °C")
        label_wea.config(text=f"Condition: {condition}")

    except:
        label_city.config(text="City not found")
        label_temp.config(text="Temperature: --")
        label_wea.config(text="Condition: --")

button = tk.Button(root, text="Get Weather", font=("Arial", 16), command=get_weather)
button.pack(pady=10)

label_city = tk.Label(root, text="City: --", font=("Arial", 16))
label_city.pack(pady=5)

label_temp = tk.Label(root, text="Temperature: --", font=("Arial", 16))
label_temp.pack(pady=5)

label_wea = tk.Label(root, text="Condition: --", font=("Arial", 16))
label_wea.pack(pady=5)

root.mainloop()
