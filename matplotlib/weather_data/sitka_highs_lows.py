from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)

header_row = next(reader)

#Extrai as temperaturas máximas/mínimas, datas
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[7])
        low = int(row[8])
    except ValueError:
        print("Missing data")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)



#Plota as temperaturas máximas e mínimas
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.7)
ax.plot(dates, lows, color='blue', alpha=0.7)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


#Formata o gráfico
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
