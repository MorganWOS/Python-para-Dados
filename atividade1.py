import numpy
array = numpy.array([i for i in range(0, 10)])
print(array)

arr = numpy.array([[i for i in range(0, 3)], [i for i in range(3, 6)],[i for i in range(6, 9)]])
print(arr)

arrf = numpy.float32([1.42, 1.2312, 2.2341, 24.43254, 2.2314231, 2.432423, 65.352532, 45.54, 44.65435, 23.3535])
print(arrf)
print(arrf.dtype)

arrb = numpy.int8([i for i in range(0, 21)])
print(arrb)
print(arrb.nbytes)

matrix = numpy.array([[1, 2, 3], [4, 5, 6]])
print(matrix, '\n')
print(matrix[0, 0], matrix[1, 2], '\n')

rangma = numpy.arange(0, 9).reshape(3,3)
rng = numpy.random.default_rng()
x = rng.permuted(rangma)
print(x)
for i in x:
    print(i.sum())

arp = numpy.array([i for i in range(0, 100, 2)])
print(arp)

x1 = numpy.random.randint(0, 100, 9)
x2 = numpy.random.randint(0, 100, 9)
x3 = numpy.random.randint(0, 100, 9)
x4 = numpy.random.randint(0, 100, 9)

b = numpy.array([])
b = numpy.append(b, (x1, x2, x3, x4)).reshape(4, 9)
print(b.reshape(6, 6))