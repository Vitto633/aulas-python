#estrutura listas

lista_numeros = [1, 2, 3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

#tipos de listas

numeros = [1, 2, 3]
strings = ["Joao", "Maria", "Arthur"]
decimais = [10.8, 15.2, 33.3]

#adicionando itens em uma lista vazia

lista_vazia = []

lista_vazia.append("ola")
lista_vazia.append("mundo")
lista_vazia.append(10)

print(lista_vazia)

#extraindo elementos da lista atravéz de métodos

lista = [1, 5, 6, 3 ,8 , 103, 59]

print("total itens na lista: ", len(lista))
print("menor valor: ", min(lista))
print("maior valor: ", max(lista))