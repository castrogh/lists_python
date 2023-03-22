inventario = []
resposta = "S"
while resposta == "S":
 inventario.append(input("Equipamento: ")) #O append tem por funcção adicionar um objeto à lista
 inventario.append(float(input("Valor: ")))
 inventario.append(int(input("Número Serial: ")))
 inventario.append(input("Departamento: "))
 resposta=input("Digite \"S\" para continuar: ").upper() #As barras invertidas antes das aspas fazem com que as aspas sejam impressas no output, sem serem interpretadas pelo código


for elemento in inventario:
    print(elemento)