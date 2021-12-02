first = float(input("digite o valor do primeiro numero: "))
second = float(input("digite o valor do segundo numero: "))
operation = input("Entre (*) para multiplicação, (/) para divisão, (+) para soma, e (-) para subtração, escolha a operação desejada: ")

if(operation == "*"):
    print("O resultado é: ",first * second)
if(operation == "/"):
    print("O resultado é: ",first / second)
if(operation == "+"):
    print("O resultado é: ",first + second)
if(operation == "-"):
    print("O resultado é: ",first - second)
