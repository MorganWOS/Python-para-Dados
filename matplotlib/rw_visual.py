import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Continua gerando passeios novos, desde que o programa esteja ativo
while True:
    #Cria um random walk
    rw = RandomWalk()
    rw.fill_walk()

    #Plota os pontos no passeio
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_number = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')

    #Destaca o primeiro e o último ponto
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove os eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break