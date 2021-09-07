import numpy



n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
det_value=numpy.linalg.det(a)

print(str(round(det_value, 11)))