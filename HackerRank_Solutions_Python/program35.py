import numpy



N,M = map(int,input().split())

A = numpy.array([input().split() for _ in range(N)], int)

min_data=numpy.min(A, axis = 1)
max_data=numpy.max(min_data)
print(max_data)