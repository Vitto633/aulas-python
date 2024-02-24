import os

mensagens = []

nome = input("Digite o seu nome: ")

while True:
    #limpando o terminal
    os.system("cls")

    if len(mensagens)> 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("------------------------")

    #obtendo o texto

    texto = input("Mensagem: ")
    if texto =="fim":
        break

    #adicionando as mensagens
    mensagens.append({
        "nome": nome,
        "texto": texto
    })