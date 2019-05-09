import time
t1 = time.time()
summ1, summ2 = 0,0
for i in range (1,101):
    summ1 += i**2
    summ2 += i
print (f'the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {summ2**2 - summ1}.')

t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')