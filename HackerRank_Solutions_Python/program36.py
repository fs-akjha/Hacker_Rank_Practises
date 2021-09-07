import numpy



N,M = map(int,input().split())

A = numpy.array([list(map(int,input().split())) for i in range(N)])

print(numpy.mean(A, axis = 1))
print(numpy.var(A, axis = 0))
std_value=numpy.std(A)
print(str(round(std_value, 11)))