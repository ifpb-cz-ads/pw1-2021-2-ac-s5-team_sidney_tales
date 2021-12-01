casa = float(input("Insira o valor da casa que deseja comprar: "))
salario = float(input("Digite o valor de seu salário: "))
years = float(input("Digite a quantidade de anos nescessarios para quitar a casa: "))

quantidade_parcelas = years * 12
valor_parcelas = casa / quantidade_parcelas

if(valor_parcelas > salario*30/100):
    print("infelizmente o emprestimo não poderá ser feito devido o valor das parcelas ultrapassarem a porcentagem minima aceita ao salario do comprador :c")
else:
    print("parabens, seu emprestimo foi aceito, o valor das parcelas sera de ",valor_parcelas,"R$, durante ",quantidade_parcelas," meses")