from pathlib import Path
import name_generator
import csv
from time import sleep



path = Path('primeiro_banco_de_dados.csv')
i = 0


#importa todos os dados que serão utilizados
names = name_generator.cria_lista_nomes()
sleep(60)
ages = name_generator.cria_lista_idade()
gen = name_generator.cria_generos()
rdr = name_generator.liked_RDR()


#Cria e escreve o banco de dados em CSV
with open('Banco_de_dados_rdr2/primeiro_banco_de_dados.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Nome,']+['Idade,']+['Sexo,']+['RDR2'])
    while i < 10000:
        try:
            spamwriter.writerow([f'{names[i]},']+ [f'{ages[i]},']+ 
                                [f'{gen[i]},']+ [f'{rdr[i]}'])
        except:
            print("Error!!!")
        i+=1
