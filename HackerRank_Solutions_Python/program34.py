import numpy



N,M = map(int,input().split())

A = numpy.array([input().split() for _ in range(N)], int)

sum_data=numpy.sum(A, axis = 0)
prod_data=numpy.prod(sum_data, axis = 0)
print(prod_data)