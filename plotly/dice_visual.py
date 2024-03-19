from die import Die
import plotly.express as px


#Cria 3 D6
die1 = Die()
die2 = Die()
die3 = Die()

#Realiza alguns testes e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

#Analisa os resultados
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualiza os resultados
title = "Results of Rolling  3 D6 1000 Times"
labels = {'x' : 'Result', 'y' : 'Frequency os Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

#Personaliza ainda mais o grafico
fig.update_layout(xaxis_dtick=1)
fig.show()