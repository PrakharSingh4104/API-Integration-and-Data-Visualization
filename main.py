import requests
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
from matplotlib.widgets import Cursor
import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os
import seaborn as sns

# --- Configuration ---
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable not set.")

# --- Helper Functions ---
def fetch_weather_data(city):
    URL = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching weather data: {e}")

def process_weather_data(data):
    times, temps, humidity = [], [], []
    for entry in data['list']:
        times.append(datetime.datetime.fromtimestamp(entry['dt']))
        temps.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])
    return times, temps, humidity

def create_weather_plot(times, temps, humidity, city):
    temp_colors = sns.color_palette("viridis", len(times)).as_hex()
    color_map = [temp_colors[min(int((t - min(temps)) / (max(temps) - min(temps) + 1e-5) * (len(temp_colors) - 1)), len(temp_colors) - 1)] for t in temps]

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#f2f2f2')
    ax.set_facecolor('#ffffff')

    for i in range(len(times) - 1):
        ax.plot(times[i:i+2], temps[i:i+2], color=color_map[i], marker='o', label='Temperature (°C)' if i == 0 else "")

    ax.plot(times, humidity, label='Humidity (%)', marker='s', color='#66b3ff')
    ax.axvline(datetime.datetime.now(), color='#ff6347', linestyle='--', label=f'Current Time: {datetime.datetime.now().strftime("%H:%M")}')

    ax.set_xlabel('Time of Day', fontsize=12, fontweight='bold', color='#333333')
    ax.set_ylabel('Value', fontsize=12, fontweight='bold', color='#333333')
    ax.set_title(f'Weather Forecast for {city}', fontsize=14, fontweight='bold', color='#333333')
    ax.tick_params(axis='x', rotation=45, colors='#333333')
    ax.tick_params(axis='y', colors='#333333')
    ax.legend(loc="upper left", frameon=False, labelcolor='#333333')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))
    ax.grid(True, linestyle='--', alpha=0.3, color='#cccccc')

    cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
    annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="lightgray"), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def on_hover(event):
        if event.inaxes == ax:
            x_vals = np.array([mdates.date2num(t) for t in times])
            y_vals = np.array(temps)
            idx = np.argmin(np.abs(x_vals - event.xdata))
            if 0 <= idx < len(times):
                annot.xy = (mdates.num2date(x_vals[idx]), y_vals[idx])
                annot.set_text(f"Time: {times[idx].strftime('%H:%M')}\nTemp: {y_vals[idx]:.1f}°C")
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                annot.set_visible(False)
                fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", on_hover)
    return fig, ax

def update_current_weather_info(data):
    current_temp = data['list'][0]['main']['temp']
    current_humidity = data['list'][0]['main']['humidity']
    weather_desc = data['list'][0]['weather'][0]['description'].capitalize()
    weather_emoji = get_weather_emoji(weather_desc.split()[0])
    return f"🌡 Temperature: {current_temp}°C\n💧 Humidity: {current_humidity}%\n☁️ Weather: {weather_desc} {weather_emoji}"

def get_weather_emoji(description):
    weather_emojis = {
        'Clear': '☀️', 'Clouds': '☁️', 'Rain': '🌧️', 'Drizzle': '🌦️', 'Thunderstorm': '⛈️', 'Snow': '❄️', 'Mist': '🌫️', 'Haze': '🌁', 'Fog': '🌫️'
    }
    return weather_emojis.get(description, '🌍')

# --- Tkinter GUI ---
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("900x700")
root.configure(bg='#2e3e4e')

# --- Styling with ttk themes ---
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background='#2e3e4e', foreground='white', font=('Segoe UI', 12))
style.configure('TButton', background='#4e5d6c', foreground='white', font=('Segoe UI', 10, 'bold'))
style.configure('TEntry', fieldbackground='#4e5d6c', foreground='white', font=('Segoe UI', 12))
style.configure('TFrame', background='#2e3e4e')
root.option_add("*TCombobox*Listbox*Background", '#4e5d6c')
root.option_add("*TCombobox*Listbox*Foreground", 'white')
root.option_add("*TCombobox*Listbox*Font", ('Segoe UI', 12))

# --- Frames ---
input_frame = ttk.Frame(root, padding=(20, 10))
input_frame.pack(pady=20)

weather_info_frame = ttk.Frame(root, padding=(10, 0))
weather_info_frame.pack()

plot_frame = ttk.Frame(root, padding=(10, 20))
plot_frame.pack(expand=True, fill=tk.BOTH)

# --- Input Elements ---
city_label = ttk.Label(input_frame, text="City:")
city_label.grid(row=0, column=0, padx=5, pady=5)

city_entry = ttk.Entry(input_frame, width=30)
city_entry.grid(row=0, column=1, padx=5, pady=5)

fetch_button = ttk.Button(input_frame, text="Get Weather", command=lambda: fetch_and_display_weather())
fetch_button.grid(row=0, column=2, padx=5, pady=5)

# --- Weather Info Label ---
weather_label = ttk.Label(weather_info_frame, text="", font=("Segoe UI", 14), wraplength=800)
weather_label.pack(pady=10)

# --- Plot Area ---
canvas_frame = plot_frame

# --- Fetch and Display Function ---
def fetch_and_display_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    try:
        data = fetch_weather_data(city)
        times, temps, humidity = process_weather_data(data)

        fig, ax = create_weather_plot(times, temps, humidity, city)

        for widget in canvas_frame.winfo_children():
            widget.destroy()  # Clear previous plot

        canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

        weather_info_text = update_current_weather_info(data)
        weather_label.config(text=weather_info_text)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

root.mainloop()  # Start the Tkinter event loop