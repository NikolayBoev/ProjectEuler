import time
t1 = time.time()
k = 4000000
n = [1,1]
i = 1
num = 0
summe = 0
while num < k:
    num = n[i] + n[i - 1]
    if n[i] % 2 == False:
        summe = summe + n[i]
    n.append(num)
    i += 1
print (summe)
t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')