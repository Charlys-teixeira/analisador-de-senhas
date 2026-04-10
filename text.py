senha = input("Digite a senha: ")


def analisar_senha(senha):
    ponto = 0
    lista = []
    simbolos = "!@#$%^&*()_+-="
    tamanho = len(senha)

    if tamanho >= 8:
        ponto += 1
    else:
        ponto -= 1
        lista.append("Senha muito curta")

    achou_numero = False
    for caractere in senha:
        if caractere.isdigit():
            achou_numero = True
    if achou_numero:
        ponto += 1
    else:
        ponto -= 1
        lista.append("Sem número")

    achou_maiuscula = False
    for caractere in senha:
        if caractere.isupper():
            achou_maiuscula = True
    if achou_maiuscula:
        ponto += 1
    else:
        ponto -= 1
        lista.append("Sem letra maiúscula")

    achou_simbolo = False
    for caractere in senha:
        if caractere in simbolos:
            achou_simbolo = True
    if achou_simbolo:
        ponto += 1
    else:
        ponto -= 1
        lista.append("Sem símbolo")

    tem_repeticao = False
    for i in range(len(senha) - 1):
        if senha[i] == senha[i + 1]:
            tem_repeticao = True
    if tem_repeticao:
        ponto -= 1
        lista.append("Tem repetição")

    tem_sequencia = False
    for i in range(len(senha) - 1):
        if (
            senha[i].isdigit()
            and senha[i + 1].isdigit()
            and int(senha[i + 1]) == int(senha[i]) + 1
        ):
            tem_sequencia = True
    if tem_sequencia:
        ponto -= 1
        lista.append("Tem sequência")

    return ponto, lista


ponto, lista = analisar_senha(senha)

if ponto <= 0:
    print("Senha fraca")
elif ponto <= 2:
    print("Senha média")
else:
    print("Senha forte")

if lista:
    print("Motivos:")
    for motivo in lista:
        print(motivo)
