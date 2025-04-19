def encripta_cesar(plain_text: str, chave: int):
    if chave < 0 or chave > 25:
        raise ValueError("A chave deve ser um número entre 0 e 25")
    lista_string = list(plain_text)
    count_letras=0
    letras = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
        8: "i",
        9: "j",
        10: "k",
        11: "l",
        12: "m",
        13: "n",
        14: "o",
        15: "p",
        16: "q",
        17: "r",
        18: "s",
        19: "t",
        20: "u",
        21: "v",
        22: "w",
        23: "x",
        24: "y",
        25: "z",
    }

    for i in range(len(plain_text)):
        letra_atual = plain_text[i].lower()
        if plain_text[i].isalpha():
            count_letras+=1
            for cod in letras.keys():
                if letras[cod] == letra_atual:
                    codigo = cod
                    break
            lista_string[i] = letras[(codigo + chave) % 26]
    print (count_letras)
    return "".join(lista_string)


def decripta_cesar(plain_text: str, chave: int):
    lista_string = list(plain_text)
    letras = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
        8: "i",
        9: "j",
        10: "k",
        11: "l",
        12: "m",
        13: "n",
        14: "o",
        15: "p",
        16: "q",
        17: "r",
        18: "s",
        19: "t",
        20: "u",
        21: "v",
        22: "w",
        23: "x",
        24: "y",
        25: "z",
    }
    for i in range(len(plain_text)):
        letra_atual = plain_text[i]
        if plain_text[i].isalpha():
            for cod in letras.keys():
                if letras[cod] == letra_atual:
                    codigo = cod
                    break
            lista_string[i] = letras[(codigo - chave) % 26]
    return "".join(lista_string)


def analise_frequencia_Cesar(texto_cifrado: str):
    # ordem de frequência de letras em português
    lista_frequencia = [
        "a",
        "e",
        "o",
        "s",
        "r",
        "i",
        "d",
        "n",
        "t",
        "c",
        "m",
        "u",
        "p",
        "l",
        "v",
        "g",
        "b",
        "f",
        "q",
        "h",
        "z",
        "j",
        "x",
        "k",
        "w",
        "y",
    ]

    # dicionário que conta a frequência de cada letra no texto cifrado
    letras_que_aparecem = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

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

    # lista para armazenar possiveis mudanças para chave de deslocamento
    indice_mudancas = [0] * 26

    # contagem da frequência de cada letra no texto cifrado
    for letra in texto_cifrado:
        if letra.isalpha():
            letras_que_aparecem[letra] += 1

    lista_tupla_frequencias = []
    for letra in letras_que_aparecem.keys():
        lista_tupla_frequencias.append((letra, letras_que_aparecem[letra]))
    lista_tupla_frequencias.sort(key=lambda x: x[1], reverse=True)

    # extração das letras mais frequentes no texto cifrado
    lista_letras_frequentes = []
    for letra in lista_tupla_frequencias:
        lista_letras_frequentes.append(letra[0])

    # cálculo das mudanças de índice entre as letras mais frequentes e a lista de frequência
    for k in range(26):
        indice = letras.index(lista_letras_frequentes[k]) - letras.index(
            lista_frequencia[k]
        )
        if indice < 0:
            indice += 26
        indice_mudancas[indice] += 1

    # ordena as tuplas de deslocamento pela frequência que o deslocamento apareceu na análise
    lista_tupla_mudancas = []
    for i in range(len(indice_mudancas)):
        lista_tupla_mudancas.append((i, indice_mudancas[i]))
    lista_tupla_mudancas.sort(key=lambda x: x[1], reverse=True)
    
    maior_mudanca = lista_tupla_mudancas[0][0]

    print(f"Chave mais provável: {maior_mudanca}")
    print(f"Texto decriptografado: {decripta_cesar(texto_cifrado, maior_mudanca)}")


def força_bruta(texto_cifrado: str):
    print ("\n")
    for i in range(26):
        print(f"Para chave {i}: {decripta_cesar(texto_cifrado, i)}\n")


def grid():
    print("O que deseja fazer?")
    print("1 - Criptografar")
    print("2 - Decriptografar")
    print("3 - Quebrar cifra por análise de frequência")
    print("4 - Quebrar cifra por força bruta")
    print("5 - Sair")


grid()
escolha = input()
if not escolha in ['1', '2', '3', '4', '5']:
    raise ValueError("A opção deve ser um número inteiro entre 1 e 5")
escolha = int(escolha)
while escolha != 5:
    if escolha == 1:
        print("Digite o texto a ser criptografado:")
        texto = input()
        print("Digite a chave:")
        chave_escolhida = int(input())
        print(f"Texto criptografado: \n{encripta_cesar(texto, chave_escolhida)}")

    elif escolha == 2:
        print("Digite o texto a ser decriptografado:")
        texto = input()
        print("Digite a chave:")
        chave_escolhida = int(input())
        print(f"Texto decriptografado: \n {decripta_cesar(texto, chave_escolhida)}")

    elif escolha == 3:
        print("Digite o texto cifrado:")
        texto = input()
        print("Texto decriptografado: \n")
        analise_frequencia_Cesar(texto)

    else:
        print("Digite o texto cifrado:")
        texto = input()
        força_bruta(texto)
    grid()
    escolha = input()
    if not escolha in ['1', '2', '3', '4', '5']:
        raise ValueError("A opção deve ser um número inteiro entre 1 e 5")
    escolha = int(escolha)
