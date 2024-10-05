#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math 

A = float(input("Me diga o valor de A dentro da equação do 2° grau: "))

# Verificar se é uma equação do segundo grau
if A == 0:
    print("A equação não é do segundo grau. Programa encerrado.")
else:
    B = float(input("Me diga o valor de B dentro da equação do 2° grau: "))
    C = float(input("Me diga o valor de C dentro da equação do 2° grau: "))

    delta = (B**2) - (4 * A * C)

    if delta < 0:
        print("A equação não possui raízes reais, pois o delta é negativo.")
    elif delta == 0:

        X = -B / (2 * A)
        print(f"A equação possui apenas uma raiz real: X = {X}")
    else:
        X1 = (-B + math.sqrt(delta)) / (2 * A)
        X2 = (-B - math.sqrt(delta)) / (2 * A)
        print(f"A equação possui duas raízes reais: X1 = {X1} e X2 = {X2}")

    print(f"A equação é: {A}*x^2 + {B}.x + {C}")
    print(f"O delta é: {delta}")
