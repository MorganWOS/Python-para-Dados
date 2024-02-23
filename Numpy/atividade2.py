import numpy as np

array = np.random.randint(-100, 100, 20)
array1 = np.array([])
array1 = np.append(array1, array)
array2 = array1.reshape(5, 4)
print(array2)


def cn(n1, n2):
    global array1
    array1 = array1.reshape(n1, n2)
    return array1.__abs__()

def qp(ar):
    s = 0
    for i in ar:
        if i < 0:
            s += 1
    return s

print(qp(array1))

def div(ma):
    s = 0
    id = 0
    id2 = 0
    for i in ma:
        id += 1
        for a in i:
            if a % 3 == 0:
                s += 1
                print(id, id2)
            id2 += 1
            if id2 >= 4:
                id2 = 0
    return s

print('numeros divisiveis por 3:')
print(div(array2), '\n')
print(array1)
def tn(a):
    index = 0
    for i in a:
        if i < 0:
            a = np.delete(a, index)
            index -= 1
        index += 1

    return a       
print(tn(array1), '\n')



def ords(a):
    a = a.flatten()
    print(a, '\n')
    index = 0
    for i in a:
        if i % 3 == 0:
            a = np.delete(a, index)
            index -= 1
        index += 1
    return a

print(ords(array2), '\n')



def ards(a):
    print('Numeros iguais')
    a = a.flatten()
    print(a, '\n')
    b = np.intersect1d(a, a)
    return b

print(ards(array2))