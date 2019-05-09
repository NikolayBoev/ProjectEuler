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
g = 10001
con = 0
i = 2
while con != 10001:
    num = primes(i)
    if len(num) == 1:
        con += 1
        if con == g:
            break
    i += 1
print (f'the 10 001st prime number is {i}.')
t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')
