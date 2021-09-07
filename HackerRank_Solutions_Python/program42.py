import numpy



N,M = map(int,input().split())

my_array = numpy.array([list(map(int,input().split())) for i in range(N)])

transpose_array=numpy.transpose(my_array)
flatten_array= my_array.flatten()

print(transpose_array)
print(flatten_array)