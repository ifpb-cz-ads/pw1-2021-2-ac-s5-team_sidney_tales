n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

menor = n1
maior = 0


if n2 < menor:
    menor = n2

if n3 < menor:
    menor = n3

if n1 >= maior:
    maior = n1

if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3


print("O numero menor é: %d" %(menor))
print("O numero maior é: %d" %(maior))
