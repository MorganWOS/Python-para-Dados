from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
from functions_weather import extraction_date_min_max as extr

import csv

path = Path('weather_data/sitka_weather_2021_full.csv')
path2 = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()
lines2 = path2.read_text().splitlines()

reader = csv.reader(lines)
reader2 = csv.reader(lines2)

reader_row = next(reader)
reader_row2 = next(reader2)


#Extrai o PRCP e as datas
dates, highs, lows = [], [], []
highs2, lows2,  dates2 = [], [], []
extr(dates, lows, highs, reader, 7, 8)
extr(dates2, lows2, highs2, reader2, 6, 7)


#Plota o PRCP
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.7)
ax.plot(dates, lows, color='blue', alpha=0.7)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.plot(dates2, highs2, color='green', alpha=0.7)
ax.plot(dates2, lows2, color='purple', alpha=0.7)
ax.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)

#Formata o gráfico
ax.set_title("Daily High and Low Temperatures, between Sitka and Death Vallei 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()