from time import time

start_time = time()

f = open('text.txt', 'w')
 
for i in range (1000000):
    f.write(str(i) + '\n')
    
f.close()

delta_t = time() - start_time

print(delta_t)