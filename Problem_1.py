import time
t1 = time.time()
n = 1000
i = 2
Sum = 0
while i < n:
    if i % 3 == False or i % 5 == False:
        Sum += i
    i += 1
print (Sum)
t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')