const apiKey = '2f18641bb6e691743a0120738b34592e'; // Replace with your OpenWeatherMap API key

async function fetchWeatherData(city) {
    const apiUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}&units=metric`;
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        return data.list.map(item => ({
            date: item.dt_txt,
            temperature: item.main.temp,
            humidity: item.main.humidity
        }));
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}

function createChart(data) {
    const ctx = document.getElementById('weatherChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(item => item.date),
            datasets: [
                {
                    label: 'Temperature (°C)',
                    data: data.map(item => item.temperature),
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    yAxisID: 'y-axis-temp',
                },
                {
                    label: 'Humidity (%)',
                    data: data.map(item => item.humidity),
                    borderColor: 'rgba(153, 102, 255, 1)',
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',
                    yAxisID: 'y-axis-humidity',
                }
            ]
        },
        options: {
            scales: {
                yAxes: [
                    {
                        id: 'y-axis-temp',
                        type: 'linear',
                        position: 'left',
                        ticks: {
                            beginAtZero: true,
                            callback: value => `${value}°C`
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Temperature (°C)'
                        }
                    },
                    {
                        id: 'y-axis-humidity',
                        type: 'linear',
                        position: 'right',
                        ticks: {
                            beginAtZero: true,
                            callback: value => `${value}%`
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Humidity (%)'
                        }
                    }
                ]
            }
        }
    });
}

async function init() {
    const fetchWeatherBtn = document.getElementById('fetchWeatherBtn');
    fetchWeatherBtn.addEventListener('click', async () => {
        const cityInput = document.getElementById('cityInput').value;
        if (cityInput) {
            const weatherData = await fetchWeatherData(cityInput);
            createChart(weatherData);
        } else {
            alert('Please enter a city name.');
        }
    });
}

document.addEventListener('DOMContentLoaded', init);
