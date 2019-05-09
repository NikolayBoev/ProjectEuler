import time
t1 = time.time()
i = 100
k = 0
while i < 1000:
    ii = 100 
    while ii < 1000:
        num = i*ii
        if str(num) == str(num)[::-1]:
            if k < num:
                k = num
        ii += 1
    i += 1
print (k)

t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')