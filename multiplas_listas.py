eqptos = []
valores = []
seriais = []
deptos = []
resp = "S"
while resp == "S":
 eqptos.append(input("Equipamento: ")) #O append tem por funcção adicionar um objeto à lista
 valores.append(float(input("Valor: ")))
 seriais.append(int(input("Número Serial: ")))
 deptos.append(input("Departamento: "))
 resp=input("Digite \"S\" para continuar: ").upper() #As barras invertidas antes das aspas fazem com que as aspas sejam impressas no output, sem serem interpretadas pelo código


for indice in range (0, len(eqptos)):
    print("\nEquipamento: ", (indice+1))
    print("Nome: ", eqptos[indice])
    print("Valor: ", valores[indice])
    print("Serial: ", seriais[indice])
    print("Departamento: ", deptos[indice])

#Para a variável “índice” que criamos no “for”, será atribuído o valor de 0 até a quantidade de elementos que existirem dentro da nossa lista “equipamentos” (função “len()”), que 
#obviamente será a mesma quantidade de elementos que existirão nas listas: valores, seriais e departamentos