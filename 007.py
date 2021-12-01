tipo = input("sendo R para residencial, C para comercial, e I para industrial, informe o tipo de seu estabelecimento: ")
amount = float(input("informe o total de energia gasto durante o periodo: "))

if(tipo == "I" or tipo == "i"):
    print("sendo um estabelecimento Industrial")

    if(amount <= 5000):
        print("O valor da conta será de ", amount*0.55,"R$")
    else:
        print("O valor da conta será de ", amount*0.60,"R$")

if(tipo == "R" or tipo == "r"):
    print("sendo um estabelecimento residencial")

    if(amount <= 500):
        print("O valor da conta será de ", amount*0.40,"R$")
    else:
        print("O valor da conta será de ", amount*0.65,"R$")

if(tipo == "C" or tipo == "c"):
    print("sendo um estabelecimento comercial")

    if(amount <= 1000):
        print("O valor da conta será de ", amount*0.55,"R$")
    else:
        print("O valor da conta será de ", amount*0.60,"R$")
