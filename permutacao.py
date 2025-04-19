import math
from itertools import permutations


def verifica_chave(chave: str):
    letras = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    dict_letras = {letra: 0 for letra in letras}
    for letra in chave:
        if letra not in letras:
            raise ValueError("A chave não pode conter caracteres especiais nem números")
        elif dict_letras[letra] > 0:
            raise ValueError("A chave não pode conter letras repetidas")
        dict_letras[letra] += 1
    if len(chave) == 0 or " " in chave:
        raise ValueError("Chave inválida")
    for letra in chave:
        if letra.isdigit():
            raise ValueError("A chave não pode conter números")


def encripta_colunar(plain_text: str, chave: str):
    lista_chave = []
    plain_text = plain_text.replace(" ", "")
    verifica_chave(chave)
    if len(plain_text) < len(chave):
        raise ValueError("A chave deve ser menor ou igual que a mensagem")
    mensagem_cifrada = ""
    index = 0

    # lista_chave usada para guardar a posição da letra na chave (qual coluna ela está associada)
    for letra in chave:
        lista_chave.append((letra.lower(), index + 1))
        index += 1

    # dicionario usado para guardar a letra e sua posição em relação a chave
    dict_chave = {index: letra for letra, index in lista_chave}

    # dicionário usado para guardar as letras do texto em claro que pertencem a mesma coluna
    dict_aux = {letra: "" for letra in chave}

    # ordena as letras da chave de acordo com sua posição no evangelho
    lista_chave_ordenada = sorted(lista_chave, key=lambda x: x[0])

    for i in range(len(plain_text)):
        index_letra = i % len(chave)
        letra_atual = dict_chave[index_letra + 1]
        dict_aux[letra_atual] += plain_text[i]
    for letra in lista_chave_ordenada:
        letra_atual = letra[0]
        mensagem_cifrada += dict_aux[letra_atual]
    return mensagem_cifrada


def decripta_colunar(cifrado: str, chave: str):
    verifica_chave(chave)
    num_linhas = len(cifrado) // len(chave)  # calcula o número de linhas da tabela
    resto_linhas = len(cifrado) % len(
        chave
    )  # calcula o 'resto' de linhas da tabela de criptografia
    tupla_linhas = []
    for letra in chave:
        tupla_linhas.append(
            (letra, num_linhas)
        )  # calcula quantas letras estão em cada coluna da tabela de criptografia, ao associar com a letra da chave
    for i in range(resto_linhas):
        tupla_linhas[i] = (
            tupla_linhas[i][0],
            tupla_linhas[i][1] + 1,
        )  # elemento [i][0]=letra, elemento [i][1]+1 = adiciona letras que estão 'sobrando' nas colunas
    dicionario_chave = {letra: "" for letra in chave}
    tupla_linhas.sort(key=lambda x: x[0])
    index = 0
    for tupla in tupla_linhas:
        letra = tupla[0]
        dicionario_chave[letra] = cifrado[
            index : tupla[1] + index
        ]  # adiciona quais letras pertencem aquela coluna
        index += tupla[1]
    mensagem_decriptada = ""
    qnt_iteracoes = math.ceil(
        len(cifrado) / len(chave)
    )  # calcula quantas linhas existem na tabela de criptografia, incluindo as linhas 'em branco'
    for j in range(
        qnt_iteracoes
    ):  # passa por todas as linhas da tabela de criptografia
        for i in range(len(chave)):
            letra = chave[i]
            if j < len(dicionario_chave[letra]):
                letra_atual = dicionario_chave[letra][
                    j
                ]  # adiciona a letra na posição [i][j] a mensagem decriptografada
                mensagem_decriptada += letra_atual

    return mensagem_decriptada


def forca_bruta_colunar(cifrado: str):  # tamanho de chave fixado em 4
    conjunto_letras = ["a", "b", "c", "d"]
    possiveis_chaves = list(permutations(conjunto_letras))
    for chave in possiveis_chaves:
        chave_junta = "".join(chave)
        print(f"Para a chave {chave_junta}: {decripta_colunar(cifrado, chave_junta)}")


def grid():
    print("O que deseja fazer?")
    print("1 - Criptografar")
    print("2 - Decriptografar")
    print("3 - Força Bruta")
    print("4 - Sair")


grid()
escolha = input("Digite a opção desejada: ")
if escolha not in ["1", "2", "3", "4"]:
    raise ValueError("Opção inválida")
escolha = int(escolha)
while escolha != 4:
    if escolha == 1:
        print("Digite a mensagem a ser criptografada: ")
        mensagem = input()
        print("Digite a chave: ")
        chave_global = input()
        print(f"Mensagem cifrada: {encripta_colunar(mensagem, chave_global)}")
    elif escolha == 2:
        print("Digite a mensagem a ser decriptografada: ")
        mensagem = input()
        print("Digite a chave: ")
        chave_global = input()
        print(f"Mensagem decriptografada: {decripta_colunar(mensagem, chave_global)}")
    elif escolha == 3:
        print("Digite a mensagem cifrada: ")
        mensagem = input()
        forca_bruta_colunar(mensagem)
    grid()
    escolha = input()
    if not escolha in ["1", "2", "3", "4"]:
        raise ValueError("Opção inválida")
    escolha = int(escolha)
