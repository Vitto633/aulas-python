notas = []
contador = 1

while contador <=5:
    codigo_aluno = input("Rm: ")
    nota = float(input("Digite a nota do aluno: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    contador +=1

print('quantidade de notas', len(notas))