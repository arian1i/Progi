import random
import numpy as np
symbols = set(chr(i) for i in range(ord('A'), ord('Z')+1)) | set(str(i) for i in range(10))
matrix = np.random.choice(list(symbols), size=(6, 6), replace=False)

print(matrix)

sentence = []
while len(sentence) < 10:
    axis = random.randint(0, 1)
    index = random.randint(0, 5)
    
if axis == 0:
    population = matrix[index]  
else:
    population = matrix[:, index]  
    
population = list(population)
   
word = ''.join(random.sample(population, random.randint(2, 5)))
    
sentence.append(word)
print(' '.join(sentence))