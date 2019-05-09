import time
t1 = time.time()
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

summe = 0
for i in range(2,2000001):
    t = primes(i)
    if len(t) == 1:
        summe += i
#print (summe)
print (f'sum of all the primes below two million is {summe}.')
t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')