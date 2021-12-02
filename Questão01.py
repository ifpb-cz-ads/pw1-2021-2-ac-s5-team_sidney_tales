velocidade = int(input("Informe a velocidade do carro: "))
valor = 0
aux = 0
if velocidade > 80:
    aux = velocidade - 80
    valor = aux * 5
    print("O valor da multa será de %d R$ " %(valor))
else: 
    print("Velocidade dentro da permitida!")

