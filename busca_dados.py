#INSERÇÃO E BUSCA DE DADOS

eqptos = []
valores = []
seriais = []
deptos = []
resp = "S"
while resp == "S":
 eqptos.append(input("Equipamento: "))
 valores.append(float(input("Valor: ")))
 seriais.append(int(input("Número Serial: ")))
 deptos.append(input("Departamento: "))
 resp = input("Digite \"S\" para continuar: ").upper()

busca = input("\nDigite o nome do equipamento que deseja visualizar: ")
for indice in range (0, len(eqptos)):
    if busca == eqptos[indice]:
        print("\nEquipamento: ", (indice+1))
        print("Nome: ", eqptos[indice])
        print("Valor: ", valores[indice])
        print("Serial: ", seriais[indice])
        print("Departamento: ", deptos[indice])