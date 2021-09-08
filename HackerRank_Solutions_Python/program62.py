import numpy
import numpy as np

def arrays(arr):
    arr.reverse()
    numpy_arr = numpy.array(arr,float)
    return numpy_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)