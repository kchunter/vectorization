import numpy as np
import time

tensor = np.random.uniform(1, 1000, 175000000)

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
    

print(vectorized_sum(tensor)) #average: 0.8
print(iterative_sum(tensor))  #average: 19.0

    
