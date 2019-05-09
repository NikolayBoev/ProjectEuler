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
       #print (n)
       primfac.append(n)
    return primfac

print (max(primes(600851475143)))

t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')