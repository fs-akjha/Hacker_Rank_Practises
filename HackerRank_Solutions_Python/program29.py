import numpy



N,M,P = map(int,input().split())

lista1=[list(map(int,input().split())) for i in range(N)]
lista2=[list(map(int,input().split())) for i in range(M)]

a1=numpy.array(lista1)
a2=numpy.array(lista2)

result=numpy.concatenate((a1, a2), axis = 0)
print(result)