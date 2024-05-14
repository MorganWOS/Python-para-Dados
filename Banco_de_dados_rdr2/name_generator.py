from random import choice
import threading
import time



vogal = ['a', 'e', 'i', 'o', 'u']
consoante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']



#Separa as vogais e consoantes
def vogais_consoantes():
    num_letras = choice([2, 3, 4, 5, 6, 7, 9])
    vogais = []
    consoantes = []
    mais_c = choice([True, False]) #mais consoantes
    if num_letras <= 5:
        if num_letras == 4:
            for i in range(2):
                consoantes.append(choice(consoante))
            for i in range(2):
                vogais.append(choice(vogal))
        if mais_c and num_letras != 4:
            for i in range(3):
                consoantes.append(choice(consoante))
            for i in range(2):
                vogais.append(choice(vogal))
        else:
            for i in range(2):
                consoantes.append(choice(consoante))
            for i in range(3):
                vogais.append(choice(vogal))
    else:
        if num_letras == 6:
            for i in range(4):
                consoantes.append(choice(consoante))
            for i in range(2):
                vogais.append(choice(vogal))
        if num_letras == 7:
            for i in range(4):
                consoantes.append(choice(consoante))
            for i in range(3):
                vogais.append(choice(vogal))
        if num_letras == 9:
            for i in range(5):
                consoantes.append(choice(consoante))
            for i in range(4):
                vogais.append(choice(vogal))

    return vogais, consoantes


#Cria os nomes
def first_name(v, s):
    name = ''
    while v or s:
        #Decide se a primeira vai ser vogal ou consoante
        v_or_s = choice(['v', 'c'])
        if v_or_s == 'v':
            if v:
                letra = choice(v)
            else:
                continue
        else:
            if s:
                letra = choice(s)
            else:
                continue
        #Adiciona a letra em 'name'
        name += letra
        #Remove a letra adicionada a 'name' de sua lista
        if v_or_s == 'v':
            v.remove(letra)
        else:
            s.remove(letra)
    return name



#Filtro de "bons" nomes
def filtro(name):
    i = 0
    while True:
        try:
            if name[i] in vogal and name[i+1] in vogal:
                return None
            if name[i] in consoante and name[i+1] in consoante:
                if name[i] in ['b', 'p', 's', 't', 'n']:
                    if name[i] in ['b', 'p', 't', 'd']:
                        if name[i+1] == 'r':
                            i += 1
                            continue
                    else:
                        i += 1
                        continue
                return None
            i += 1
        except:
            break
    return name


#Cria a lista de nomes
name_list = []
def cria_lista_nomes():
    while len(name_list) < 10000:
        name = filtro(first_name(vogais_consoantes()[0], vogais_consoantes()[1]))
        if name != None:
            name_list.append(name.capitalize())
        else:
            continue
    return name_list


#Cria a lista de idades 
number_list = []
def cria_lista_idade():
    while len(number_list) < 10000:
        idade = choice(range(18, 80))
        number_list.append(idade)
    return number_list



#Defini o genero dos nomes
gen_list = []
def cria_generos():
    while len(gen_list) < 10000:
        for i in name_list:
            if i[-1] in ('a', 'u', 'i'):
                gen_list.append('F')
            elif i[-1] in ('o', 'e'):
                gen_list.append('M')
            else:
                gen_list.append(choice(('F', 'M')))
    return gen_list



#Se gosta de Red Dead Redenption 2
rdr = []
def liked_RDR():
    while len(rdr) < 10000:
        rdr.append(choice(('Y', 'N')))
    return rdr


#Definição de threads
t1 = threading.Thread(target=cria_generos)
t2 = threading.Thread(target=cria_lista_idade)


#cria_lista_nomes()
#time.sleep(40)
#liked_RDR()
#t1.start()
#t2.start()