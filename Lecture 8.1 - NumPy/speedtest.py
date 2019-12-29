import numpy as np
import timeit
from datetime import datetime
startTime = datetime.now()

arr = np.ones((1000, 1000))

sum = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        sum += arr[i, j]
print(sum)

print("Loop-based implementation time: " + str(datetime.now() - startTime))

startTime = datetime.now()

arr = np.ones((1000, 1000))

print(np.sum(arr))

print("Numpy-operation-based implementation time: " + str(datetime.now() - startTime))



