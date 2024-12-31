def sqrt(a):
    i = 0
    while i*i <= a:
        i = i+1
    return i-1

num = ((600851475143)/71)/839/1471
print(num)

i= 3
fatores = [ ]
while i <= sqrt(num):
    if num%i == 0:
        fatores.append(i)
    i = i+2
    print(i,fatores)
