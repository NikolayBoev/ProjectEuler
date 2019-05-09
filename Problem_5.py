import time
t1 = time.time()
def check_divisible(n):
    i = 1
    count = 0
    while i <= 20:
        if n % i:
            break
        else:
            count += 1
        i += 1
    return count

ii = 1
num = 0
while num != 20:
    num = check_divisible(ii)
    if num > 19:
        print (ii, num)
    ii += 1
t1 = round((time.time() - t1)*1000,4)
print (f'the solution took {t1} ms')