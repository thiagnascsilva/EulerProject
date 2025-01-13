import time
start_time = time.time()
print("\033c\033[3J", end='')


def sqrt(a):
    i = 0
    while i*i <= a:
        i = i+1
    return i-1


def isprime(a):
    i = 2
    while i <= sqrt(a):
        if a % i == 0:
            return 0
        i = i+1
    return 1


i = 2
primos_teste = []
while i <= 350:
    if isprime(i) == 1:
        primos_teste.append(i)
    i = i+1


def tprime(a):
    i = 0
    while i < len(primos_teste):
        if a % primos_teste[i] == 0:
            return 0
        i = i+1
    return 1

j = 2
p = 1
primos = []
while len(primos) < 10001-70:
    if tprime(j) == 1:
        primos.append(j)
        if p+70 == 10001:
            print(p+70, j)
        p = p+1
    j = j+1
print("--- %s seconds ---" % (time.time() - start_time))
