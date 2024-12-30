def fib(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    else:
        return fib(a-1)+fib(a-2)


i = 1
sum = 0
while fib(i) <= 4000000:
    if fib(i) % 2 == 0:
        sum = sum+fib(i)
    i = i+1
print(sum)
