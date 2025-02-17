# API-Integration-and-Data-Visualization

*COMPANY*: CODTECH IT SOLUTIONS 

*NAME*: PRAKHAR SINGH 

*INTERN ID*: CT08QIO

*DOMAIN*: PYTHON PROGRAMING 

*DURATION*: 4 WEEEKS 

*MENTOR*: NEELA SANTOSH


## DESCRIPTION


# Weather Data Visualization

This repository contains a project that fetches weather data from the OpenWeatherMap API and visualizes it through interactive graphs. The project uses HTML, CSS, JavaScript for the frontend, and Python for more advanced data processing and visualization. It is designed to provide real-time weather information for any city, with a focus on temperature and humidity data.

## Features

- 🌦 **Weather Data Fetching**: The project fetches weather data from OpenWeatherMap, an API that provides global weather information. The weather data includes temperature, humidity, and weather descriptions.
  
- 📊 **Frontend Visualization**: The frontend of the project uses HTML, CSS, and JavaScript to provide an intuitive and responsive user interface. Users can input a city name, click a button to fetch the weather data, and view a real-time line graph displaying both the temperature (°C) and humidity (%) over time. The chart updates dynamically based on the city input.

- 📈 **Interactive Chart**: The data is displayed on a line chart using the popular JavaScript charting library, **Chart.js**. The chart has two y-axes to show both temperature and humidity. The data points are color-coded, with temperature data being represented with a gradient and humidity data shown as a separate line in blue. The chart is interactive, allowing users to hover over data points to see precise details about the temperature and time.

- 🐍 **Python Backend for Data Processing**: The project includes a Python script that uses the `requests` library to fetch data from OpenWeatherMap, processes the data, and visualizes it using `Matplotlib` and `Seaborn`. The Python backend provides more advanced visualization features, including color palettes and enhanced interactivity.

- 🖥️ **Tkinter GUI**: The Python version of the project is further enhanced with a graphical user interface (GUI) built using Tkinter. Users can input a city name and view both real-time weather information (temperature, humidity, and weather description) and an interactive plot inside the same window. The GUI is styled for a sleek, modern look, with error handling and user-friendly prompts to ensure a smooth experience.

## Installation

To run this project locally, follow these steps:

### Prerequisites

- 🌍 **For the frontend (HTML, CSS, JavaScript)**: No installation is required. Simply open the `index.html` file in a browser to view the weather data visualization.
  
- 🐍 **For the Python backend**:
  - Install Python (preferably Python 3.7 or later).
  - Install the required Python libraries.
  - Set your OpenWeatherMap API key in your environment variables. Replace the placeholder with your actual OpenWeatherMap API key. You can sign up for a free API key on the [OpenWeatherMap website](https://openweathermap.org/).

### Running the Project

- 🖥️ **Frontend (HTML, CSS, JavaScript)**: Simply open the `index.html` file in a browser to start the project.
- 🐍 **Backend (Python)**: Run the `weather_gui.py` file using Python. The Tkinter application will open, allowing you to input a city name and view the weather forecast.

## Usage

- 🌆 **Input a City Name**: Enter a valid city name in the input field and press the "Get Weather" button.
- 🌞 **View Weather Information**: The current temperature, humidity, and weather description will be displayed below the input field.
- 🌡️ **View Weather Plot**: An interactive graph will be displayed with temperature and humidity data over time.
- 🖱️ **Hover Over the Graph**: Hover over data points on the graph to see precise temperature and time information.

## Acknowledgments

- 🌍 **OpenWeatherMap**: For providing the weather data API.
- 📊 **Chart.js**: For providing an interactive charting library.
- 📉 **Matplotlib & Seaborn**: For creating advanced data visualizations in Python.
- 🖥️ **Tkinter**: For building the GUI application.

