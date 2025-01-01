def my_function(x):
    return x[::-1]


maior = 0
i = 100
numeros = []
while i <= 999:
    j = 100
    while j <= 999:
        if str(i*j) == str(my_function(str(i*j))):
            if i*j >= maior:
                maior = i*j
                numeros.append(maior)
        j = j+1
    i = i+1
print(numeros)
