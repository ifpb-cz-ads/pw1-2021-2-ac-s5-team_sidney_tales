salario = float(input("Informe o salário: "))
aumento = 0
salarioReajuste = 0

if salario > 1250:
    aumento = salario * 0.1
    salarioReajuste = aumento + salario

else:
    aumento = salario * 0.15
    salarioReajuste = aumento + salario

print("O aumento foi de %.2f R$ e o salario reajustado será de: %.2f R$" %(aumento, salarioReajuste))