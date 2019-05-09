import time
t1 = time.time()
from math import sqrt
product = 0
for a in range (1,500):
    for b in range (1,500):
        c = sqrt(a**2 + b**2)
        if a+b+c ==1000:
            print (a,b,c, a*b*c)
            product = a*b*c
            break
print (f'the product is {product}.')
t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')