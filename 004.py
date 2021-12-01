distancia = float(input("Informe o distancia total da viagem: "))

if(distancia <= 200):
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print("para a viagem com distancia igual ",distancia,"KM, passagem tera um valor de ",passagem,"R$")