num = int(input('Digite um número para ver sua tabuada:'))
x = 1
while x <= 10:
    print('{} x {} = {}'.format(num, x, num*x))
    x = x + 1
    