n = 1
p = 0
i = 0

while n <= 20:
    a = int(input("Digite os numero: "))
    n = n + 1
    if a % 2 == 0:
        a = p
        p = p + 1
    else:
        a = i
        i = i + 1

print("A quantidade de numeros pares e: ",p)
print("A quantidade de numeros inpares e: ",i)