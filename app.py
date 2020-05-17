import requests
import ctypes
import datetime
import time
from datetime import date

SPI_SETDESKWALLPAPER = 20

# Set to the file path of your images
path_to_folder = r"C:\PATH TO FILE"

# Get a weather API key at https://openweathermap.org/api
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&q="

# Enter your location
city = "WHERE YOU LIVE"

url = api_address + city


def main():
    timestamp = datetime.datetime.now().time()
    start_night = datetime.time(18, 1)
    end_night = datetime.time(6, 0)
    start_day = datetime.time(6, 1)
    end_day = datetime.time(18, 0)
    json_data = requests.get(url).json()
    format_data = json_data["weather"][0]["main"]

    if date.today().weekday() == 6:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Tokyo.jpg", 3)
    elif format_data == "Rain":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Waterfall.jpg", 3)
    elif format_data == "Thunderstorm":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Cloud.jpg", 3)
    elif format_data == "Drizzle":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Rooftop1.png", 3)

    # Night & Day
    elif format_data == "Clear" and start_night <= timestamp or timestamp <= end_night:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Moon.png", 3)
    elif format_data == "Clear" and start_day <= timestamp <= end_day:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\KatanaMorning.png", 3)

    elif format_data == "Clouds":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Shibuya.png", 3)
    else:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Firewatch.jpg", 3)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(120)
