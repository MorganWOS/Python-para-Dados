from pathlib import Path
import csv
import matplotlib.pyplot as plt


path = Path('archive(1)/Console_Data.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)

header_row = next(reader)


print(header_row)

consoles, consoles_solds, years, companys, bar_colors = [], [], [], [], []

for row in reader:
    console = row[0]
    year = int(row[5])
    console_sold = float(row[8])
    company = row[2]
    
    consoles.append(console)
    years.append(year)
    consoles_solds.append(console_sold)

    if company == 'Sony':
        bar_colors.append('tab:blue')
    if company == 'Nintendo':
        bar_colors.append('tab:red')
    if company == 'Microsoft':
        bar_colors.append('tab:green')
    if company == 'Magnavox':
        bar_colors.append('tab:orange')
    if company == 'Atari':
        bar_colors.append('tab:brown')
    if company == 'Sega':
        bar_colors.append('tab:purple')
    if company == 'Mattel':
        bar_colors.append('tab:grey')





plt.style.use('classic')
fig, ax = plt.subplots()
ax.bar(consoles, consoles_solds, width=1,  edgecolor="black", linewidth=1, color=bar_colors )


title = 'Video-Games consoles sold'
ax.set_title(title, fontsize=24)
ax.set_xlabel('Consoles', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Solds(m)', fontsize=14)
ax.tick_params(labelsize=16)

plt.show()