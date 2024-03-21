from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt

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
dates, prcps = [], []
prcps2, dates2 = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp = float(row[5])
    except ValueError:
        print("Missing data")
    else:
        prcps.append(prcp)
        dates.append(current_date)
for row in reader2:
    current_date2 = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp = float(row[3])
    except ValueError:
        print("Missing data")
    else:
        prcps2.append(prcp)   
        dates2.append(current_date2)

#Plota o PRCP
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='green', alpha=1)
ax.plot(dates, prcps2, color='blue', alpha=1)

#Formata o gráfico
ax.set_title("Daily PRCP in Sitka and Death Valley, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("PRCP", fontsize=20)
ax.tick_params(labelsize=16)

plt.show()