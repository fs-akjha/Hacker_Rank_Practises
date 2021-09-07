import numpy



A = numpy.array(input().split(),int)
B = numpy.array(input().split(),int)

inner_product=numpy.inner(A, B)
outer_product=numpy.outer(A, B)

print(inner_product)
print(outer_product)