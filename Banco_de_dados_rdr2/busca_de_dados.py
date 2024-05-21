from pathlib import Path
import csv
import matplotlib.pyplot as plt


path = Path('/home/morganwos/Programacao_Estudos/RDR2/primeiro_banco_de_dados.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)

header_row = next(reader)

print(header_row)


#Cria as listas para dados 
names, years, gens, likes = [], [], [], []

#Faz o loop para passar pelo arquivo e armazenar aos dados nas listas certas
for row in reader:
    year = int(row[1])
    name = row[0]
    gen = row[2]
    like_R = row[3]

    years.append(year)
    names.append(name)
    gens.append(gen)
    likes.append(like_R)


y = likes.count(' Y')
n = likes.count(' N')

m = gens.count(' M')
f = gens.count(' F')


print("Pessoas que gostam de RDR2:")
print(y)



#Cria a visualização grafica dos dados coletados
fig, ax = plt.subplots()

ax.bar(['Y', 'N'], [y, n], color=['pink', 'blue'])

ax.set_title("Sexo dos participantes")

plt.show()
