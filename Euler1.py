def m35(a):
    if a % 3 == 0 or a % 5 == 0:
        return 1
    else:
        return 0
    
i = 0
sum = 0
while i < 1000:
    if m35(i) == 1:
        sum = sum+i
    i = i+1
print(sum)