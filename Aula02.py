import os
os.system("cls")

# idade = int(input("Digite idade: "))
#
# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")

# numero = int(input("Numero: "))

# if numero < 0:
#     print("Negativo")
# else:
#     if numero > 0:
#         print("Positivo")
#     else:
#         print("Nulo")

# if numero < 0:
#     print("Negativo")
# elif numero > 0:
#     print("Positivo")
# else:
#     print("Nulo")

# Comando de seleção ( swtich )

# numero = int(input("Numero: "))

print("""
1 -Enunciado do exercicio 1
2- Enunciado do exercicio 2
3- Enunciado do exercicio 3
4- Enunciado do exericcio 4
    """)


opcao = int(input("Escolha: "))

match opcao:
    case 1:
        print("executando o exercicio1")
    case 2:
        print("Executando o exercicio2")
    case 3:
        print("Executando o exercicio3")
    case 4:
        print("Executando o exericcio4")
    case _:
        print("erro")



