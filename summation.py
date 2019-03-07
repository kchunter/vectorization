import numpy as np
import time

tensor = np.random.uniform(0, 1, 200000000)

def vectorized_sum(tensor):

    start_time = time.time()

    ones = np.ones(tensor.size)
    np.dot(tensor, ones)
        
    end_time = time.time()
    return end_time - start_time

def iterative_sum(tensor):
    
    start_time = time.time()

    summation = 0
    for j in tensor:
        summation += j
        
    end_time = time.time()
    return end_time - start_time
    

print(vectorized_sum(tensor)) #average: 0.86 s
print(iterative_sum(tensor))  #average: 19.4 s

    
