# programa condicional permissao

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("PERMITIDO!")
else:
    print("BLOQUEADO!")


# programa condicional salário

salario = float(input("Digite o seu salario: "))

if salario <=3000:
    print("Programador Junior.")
elif salario > 3000 and salario <=6000:
    print("Programador Pleno.")
elif salario > 6000 and salario <= 15000:
    print("Programador senior.")
else:
    print("Gerente de projetos.")