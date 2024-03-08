import matplotlib.pyplot as plt

x_value = range(1, 5001)
y_value = [x**3 for x in x_value]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10)

#define o tíulo do gráfico e os eixos
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square Value", fontsize=14)

#Define o tamanho dos rotulos e marcação de escala
ax.tick_params(labelsize=14)

#Define o intervalo para cada eixo
ax.axis([0, 5000, 0, 128_900_500_000])
ax.ticklabel_format(style='plain')

plt.show()