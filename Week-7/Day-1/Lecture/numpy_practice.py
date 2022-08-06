import numpy as np

arr = np.array([1,2,3,4,5])

def practice (array):
    return array.min(), array.std(), np.prod(array), np.dot(array, array), array-4


print(practice(arr))