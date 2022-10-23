import os

print("\n -CALCULADORA- \n")

operacao = str(input("Selecione a operacao desejada:\n 1-SOMA\n 2-SUBTRACAO\n 3-MULTIPLICACAO\n 4-DIVISAO\n Digite aqui: "))
n1 = int(input("\nDigite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
resultado = 0

if operacao == "1" or operacao == "SOMA" or operacao == "Soma" or operacao == "soma":
    resultado = n1+n2
    print("RESULTADO: {}\n".format(resultado))
    os.system('pause'), os.system('cls')

elif operacao == "2" or operacao == "SUBTRACAO" or operacao == "Subtracao" or operacao == "subtracao":
    resultado = n1-n2
    print("RESULTADO: {}\n".format(resultado))
    os.system('pause'), os.system('cls')

elif operacao == "3" or operacao == "MULTIPLICACAO" or operacao == "Multiplicacao" or operacao == "multiplicacao":
    resultado = n1*n2
    print("RESULTADO: {}\n".format(resultado))
    os.system('pause'), os.system('cls')

elif operacao == "4" or operacao == "DIVISAO" or operacao == "Divisao" or operacao == "divisao":
    resultado = n1/n2
    print("RESULTADO: {:.2f}\n".format(float(resultado)))
    os.system('pause'), os.system('cls')

else:
    print("Algo deu errado!")