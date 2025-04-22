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
        if not letra.isalpha():
            raise ValueError(
                "A chave não pode conter caracteres especiais, números e nem espaços"
            )
        elif dict_letras[letra] > 0:
            raise ValueError("A chave não pode conter letras repetidas")
        dict_letras[letra] += 1
    if len(chave) == 0:
        raise ValueError("Chave inválida")


def encripta_colunar(plain_text: str, chave: str):
    lista_chave = []
    verifica_chave(chave)
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
        if plain_text[i].isalpha():
            letra_add = plain_text[i].lower()
            dict_aux[letra_atual] += letra_add
        else:
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


def acha_digrafos(frase: str):  # função que acha todos os dígrafos em um texto
    frase = frase.lower()
    palavras = frase.split()
    pares = []
    for i in palavras:
        for j in range(len(i) - 1):
            par = i[j : j + 2]
            pares.append(par)
    return pares


def acha_trigrafos(frase: str):
    frase = frase.lower()
    palavras = frase.split()
    trigrafos = []
    for i in palavras:
        for j in range(len(i) - 2):
            par = i[j : j + 3]
            trigrafos.append(par)
    return trigrafos


trigrafos_pt = {
    "que": 72.29,
    "ent": 70.23,
    "nte": 55.08,
    "ado": 51.16,
    "ade": 50.04,
    "ode": 45.43,
    "ara": 45.37,
    "est": 43.90,
    "res": 43.08,
    "con": 41.73,
    "com": 40.95,
    "sta": 30.95,
    "dos": 38.08,
    "cao": 37.97,
    "par": 36.29,
    "aca": 35.55,
    "men": 34.65,
    "sde": 33.45,
    "ica": 33.05,
    "ese": 31.87,
    "aco": 31.54,
    "ada": 31.45,
    "por": 31.39,
    "nto": 31.14,
    "ose": 30.82,
    "des": 30.51,
    "ase": 27.76,
    "era": 27.18,
    "oes": 26.60,
    "uma": 25.73,
    "tra": 25.66,
    "lda": 25.55,
    "dad": 24.84,
    "ant": 24.54,
    "are": 24.30,
    "ont": 24.05,
    "pre": 24.04,
    "ist": 23.91,
    "ter": 23.89,
    "als": 23.37,
}


def dict_digrafos():  # dicionario com a frequencia de ocorrencia de cada dígrafo na lingua portuguesa
    digrafos_pt = {
        "aa": 5.13,
        "ab": 2.35,
        "ac": 10.05,
        "ad": 14.80,
        "ae": 4.49,
        "af": 2.27,
        "ag": 2.14,
        "ah": 0.48,
        "ai": 5.11,
        "aj": 0.57,
        "ak": 0.09,
        "al": 9.03,
        "am": 8.08,
        "an": 11.62,
        "ao": 11.84,
        "ap": 5.84,
        "aq": 1.85,
        "ar": 14.89,
        "as": 16.41,
        "at": 5.01,
        "au": 2.26,
        "av": 3.04,
        "aw": 0.04,
        "ax": 0.15,
        "ay": 0.08,
        "az": 0.84,
        "ba": 1.90,
        "bb": 0.02,
        "bc": 0.03,
        "bd": 0.02,
        "be": 1.90,
        "bf": 0.00,
        "bg": 0.00,
        "bh": 0.00,
        "bi": 1.02,
        "bj": 0.10,
        "bk": 0.00,
        "bl": 0.83,
        "bm": 0.03,
        "bn": 0.00,
        "bo": 1.26,
        "bp": 0.02,
        "bq": 0.00,
        "br": 1.83,
        "bs": 0.22,
        "bt": 0.07,
        "bu": 0.46,
        "bv": 0.02,
        "bw": 0.00,
        "bx": 0.00,
        "by": 0.01,
        "bz": 0.00,
        "ca": 12.57,
        "cb": 0.01,
        "cc": 0.45,
        "cd": 0.07,
        "ce": 3.78,
        "cf": 0.01,
        "cg": 0.01,
        "ch": 1.12,
        "ci": 6.09,
        "cj": 0.00,
        "ck": 0.09,
        "cl": 0.00,
        "cm": 0.02,
        "cn": 0.15,
        "co": 14.00,
        "cp": 0.10,
        "cq": 0.02,
        "cr": 1.38,
        "cs": 0.03,
        "ct": 1.62,
        "cu": 1.68,
        "cv": 0.00,
        "cw": 0.00,
        "cx": 0.00,
        "cy": 0.00,
        "cz": 0.00,
        "da": 11.92,
        "db": 0.02,
        "dc": 0.03,
        "dd": 0.05,
        "de": 20.33,
        "df": 0.01,
        "dg": 0.02,
        "dh": 0.02,
        "di": 4.96,
        "dj": 0.04,
        "dk": 0.00,
        "dl": 0.02,
        "dm": 0.20,
        "dn": 0.03,
        "do": 14.45,
        "dp": 0.05,
        "dq": 0.03,
        "dr": 0.50,
        "ds": 0.07,
        "dt": 0.02,
        "du": 1.13,
        "dv": 0.07,
        "dw": 0.01,
        "dx": 0.00,
        "dy": 0.02,
        "dz": 0.00,
        "ea": 6.34,
        "eb": 0.95,
        "ec": 7.25,
        "ed": 5.77,
        "ee": 3.34,
        "ef": 2.17,
        "eg": 2.81,
        "eh": 0.44,
        "ei": 5.31,
        "ej": 0.89,
        "ek": 0.07,
        "el": 5.97,
        "em": 10.92,
        "en": 14.94,
        "eo": 3.24,
        "ep": 3.99,
        "eq": 1.66,
        "er": 13.33,
        "es": 20.71,
        "et": 3.53,
        "eu": 3.28,
        "ev": 2.35,
        "ew": 0.08,
        "ex": 1.52,
        "ey": 0.06,
        "ez": 0.73,
        "fa": 1.56,
        "fb": 0.00,
        "fc": 0.04,
        "fd": 0.01,
        "fe": 2.03,
        "ff": 0.04,
        "fg": 0.00,
        "fh": 0.00,
        "fi": 2.64,
        "fj": 0.00,
        "fk": 0.00,
        "fl": 0.21,
        "fm": 0.01,
        "fn": 0.01,
        "fo": 2.21,
        "fp": 0.02,
        "fq": 0.00,
        "fr": 0.81,
        "fs": 0.01,
        "ft": 0.03,
        "fu": 0.64,
        "fv": 0.00,
        "fw": 0.00,
        "fx": 0.00,
        "fy": 0.00,
        "fz": 0.00,
        "ga": 2.60,
        "gb": 0.01,
        "gc": 0.02,
        "gd": 0.03,
        "ge": 1.74,
        "gf": 0.01,
        "gg": 0.01,
        "gh": 0.04,
        "gi": 1.22,
        "gj": 0.00,
        "gk": 0.01,
        "gl": 0.13,
        "gm": 0.03,
        "gn": 0.21,
        "go": 2.05,
        "gp": 0.02,
        "gq": 0.00,
        "gr": 1.56,
        "gs": 0.03,
        "gt": 0.05,
        "gu": 2.52,
        "gv": 0.00,
        "gw": 0.00,
        "gx": 0.00,
        "gy": 0.00,
        "gz": 0.00,
        "ha": 2.70,
        "hb": 0.00,
        "hc": 0.02,
        "hd": 0.02,
        "he": 1.44,
        "hf": 0.01,
        "hg": 0.00,
        "hh": 0.02,
        "hi": 0.53,
        "hj": 0.00,
        "hk": 0.02,
        "hl": 0.03,
        "hm": 0.06,
        "hn": 0.00,
        "ho": 2.26,
        "hp": 0.01,
        "hq": 0.00,
        "hr": 0.03,
        "hs": 0.01,
        "ht": 0.04,
        "hu": 0.24,
        "hv": 0.00,
        "hw": 0.00,
        "hx": 0.00,
        "hy": 0.00,
        "hz": 0.00,
        "ia": 8.15,
        "ib": 0.67,
        "ic": 6.83,
        "id": 5.54,
        "ie": 1.16,
        "if": 0.85,
        "ig": 1.50,
        "ih": 0.02,
        "ii": 0.11,
        "ij": 0.05,
        "ik": 0.05,
        "il": 2.52,
        "im": 3.70,
        "in": 8.22,
        "io": 4.84,
        "ip": 1.07,
        "iq": 0.18,
        "ir": 4.50,
        "is": 8.79,
        "it": 4.90,
        "iu": 0.65,
        "iv": 2.50,
        "iw": 0.00,
        "ix": 0.45,
        "iy": 0.00,
        "iz": 1.31,
        "ja": 1.14,
        "jb": 0.00,
        "jc": 0.00,
        "jd": 0.00,
        "je": 0.55,
        "jf": 0.00,
        "jg": 0.00,
        "jh": 0.00,
        "ji": 0.03,
        "jj": 0.00,
        "jk": 0.00,
        "jl": 0.00,
        "jm": 0.00,
        "jn": 0.00,
        "jo": 1.04,
        "jp": 0.00,
        "jq": 0.00,
        "jr": 0.00,
        "js": 0.00,
        "jt": 0.00,
        "ju": 0.00,
        "jv": 0.00,
        "jw": 0.00,
        "jx": 0.00,
        "jy": 0.00,
        "jz": 0.00,
        "ka": 0.10,
        "kb": 0.00,
        "kc": 0.01,
        "kd": 0.01,
        "ke": 0.01,
        "kf": 0.00,
        "kg": 0.02,
        "kh": 0.10,
        "ki": 0.00,
        "kj": 0.01,
        "kk": 0.02,
        "kl": 0.02,
        "km": 0.01,
        "kn": 0.09,
        "ko": 0.01,
        "kp": 0.00,
        "kq": 0.02,
        "kr": 0.03,
        "ks": 0.01,
        "kt": 0.02,
        "ku": 0.00,
        "kv": 0.00,
        "kw": 0.00,
        "kx": 0.00,
        "ky": 0.00,
        "kz": 0.00,
        "la": 4.93,
        "lb": 0.15,
        "lc": 0.52,
        "ld": 1.32,
        "le": 3.96,
        "lf": 0.18,
        "lg": 0.59,
        "lh": 1.92,
        "li": 5.22,
        "lj": 0.06,
        "lk": 0.02,
        "ll": 0.31,
        "lm": 0.78,
        "ln": 0.24,
        "lo": 3.43,
        "lp": 0.45,
        "lq": 0.31,
        "lr": 0.10,
        "ls": 0.35,
        "lt": 1.39,
        "lu": 1.16,
        "lv": 0.56,
        "lw": 0.00,
        "lx": 0.00,
        "ly": 0.04,
        "lz": 0.00,
        "ma": 11.35,
        "mb": 1.48,
        "mc": 1.08,
        "md": 1.29,
        "me": 8.13,
        "mf": 0.37,
        "mg": 0.20,
        "mh": 0.12,
        "mi": 3.37,
        "mj": 0.16,
        "mk": 0.01,
        "ml": 0.30,
        "mm": 0.66,
        "mn": 0.54,
        "mo": 5.21,
        "mp": 3.49,
        "mq": 0.58,
        "mr": 0.38,
        "ms": 0.86,
        "mt": 0.54,
        "mu": 1.88,
        "mv": 0.27,
        "mw": 0.01,
        "mx": 0.00,
        "my": 0.01,
        "mz": 0.00,
        "na": 8.65,
        "nb": 0.04,
        "nc": 4.47,
        "nd": 5.27,
        "ne": 2.24,
        "nf": 0.72,
        "ng": 1.05,
        "nh": 1.91,
        "ni": 3.43,
        "nj": 0.14,
        "nk": 0.07,
        "nl": 0.04,
        "nm": 0.05,
        "nn": 0.13,
        "no": 6.13,
        "np": 0.06,
        "nq": 0.25,
        "nr": 0.10,
        "ns": 0.36,
        "nt": 13.27,
        "nu": 1.30,
        "nv": 0.64,
        "nw": 0.01,
        "nx": 0.00,
        "ny": 0.03,
        "nz": 0.06,
        "oa": 5.41,
        "ob": 2.08,
        "oc": 5.37,
        "od": 9.58,
        "oe": 6.29,
        "of": 1.89,
        "og": 1.73,
        "oh": 0.47,
        "oi": 2.79,
        "oj": 0.83,
        "ok": 0.06,
        "ol": 3.66,
        "om": 7.79,
        "on": 10.14,
        "oo": 2.04,
        "op": 6.30,
        "oq": 1.84,
        "or": 11.85,
        "os": 18.26,
        "ot": 2.55,
        "ou": 0.06,
        "ov": 2.24,
        "ow": 0.08,
        "ox": 0.25,
        "oy": 0.03,
        "oz": 0.16,
        "pa": 6.74,
        "pb": 0.00,
        "pc": 0.17,
        "pd": 0.05,
        "pe": 5.23,
        "pf": 0.02,
        "pg": 0.01,
        "ph": 0.04,
        "pi": 0.93,
        "pj": 0.01,
        "pk": 0.00,
        "pl": 0.86,
        "pm": 0.02,
        "pn": 0.03,
        "po": 7.46,
        "pp": 0.10,
        "pq": 0.02,
        "pr": 6.02,
        "ps": 0.26,
        "pt": 0.21,
        "pu": 0.93,
        "pv": 0.01,
        "pw": 0.00,
        "px": 0.00,
        "py": 0.00,
        "pz": 0.00,
        "qa": 0.00,
        "qb": 0.00,
        "qc": 0.00,
        "qd": 0.00,
        "qe": 0.00,
        "qf": 0.00,
        "qg": 0.00,
        "qh": 0.00,
        "qi": 0.00,
        "qj": 0.00,
        "qk": 0.00,
        "ql": 0.00,
        "qm": 0.00,
        "qn": 0.00,
        "qo": 0.00,
        "qp": 0.00,
        "qq": 0.00,
        "qr": 0.00,
        "qs": 0.00,
        "qt": 0.00,
        "qu": 0.00,
        "qv": 0.00,
        "qw": 0.00,
        "qx": 0.00,
        "qy": 0.00,
        "qz": 0.00,
        "ra": 17.43,
        "rb": 0.28,
        "rc": 2.34,
        "rd": 2.41,
        "re": 14.16,
        "rf": 0.31,
        "rg": 0.92,
        "rh": 0.07,
        "ri": 8.06,
        "rj": 0.10,
        "rk": 0.05,
        "rl": 0.41,
        "rm": 1.88,
        "rn": 1.61,
        "ro": 8.11,
        "rp": 0.85,
        "rq": 0.81,
        "rr": 1.84,
        "rs": 1.31,
        "rt": 3.73,
        "ru": 1.53,
        "rv": 0.66,
        "rw": 0.01,
        "rx": 0.00,
        "ry": 0.05,
        "rz": 0.02,
        "sa": 9.19,
        "sb": 0.66,
        "sc": 4.18,
        "sd": 6.33,
        "se": 13.47,
        "sf": 1.19,
        "sg": 0.39,
        "sh": 0.57,
        "si": 4.72,
        "sj": 0.38,
        "sk": 0.06,
        "sl": 0.65,
        "sm": 2.37,
        "sn": 1.82,
        "so": 5.91,
        "sp": 5.20,
        "sq": 1.47,
        "sr": 1.05,
        "ss": 6.33,
        "st": 9.80,
        "su": 2.58,
        "sv": 0.63,
        "sw": 0.02,
        "sx": 0.00,
        "sy": 0.00,
        "sz": 0.00,
        "ta": 11.46,
        "tb": 0.01,
        "tc": 0.09,
        "td": 0.03,
        "te": 12.72,
        "tf": 0.01,
        "tg": 0.01,
        "th": 0.15,
        "ti": 6.17,
        "tj": 0.01,
        "tk": 0.00,
        "tl": 0.07,
        "tm": 0.06,
        "tn": 0.04,
        "to": 9.33,
        "tp": 0.07,
        "tq": 0.01,
        "tr": 5.83,
        "ts": 0.11,
        "tt": 0.12,
        "tu": 2.94,
        "tv": 0.03,
        "tw": 0.01,
        "tx": 0.00,
        "ty": 0.02,
        "tz": 0.02,
        "ua": 3.98,
        "ub": 1.01,
        "uc": 1.05,
        "ud": 1.22,
        "ue": 8.55,
        "uf": 0.14,
        "ug": 0.87,
        "uh": 0.03,
        "ui": 2.55,
        "uj": 0.15,
        "uk": 0.02,
        "ul": 2.15,
        "um": 5.54,
        "un": 3.20,
        "uo": 0.51,
        "up": 0.96,
        "uq": 0.18,
        "ur": 2.72,
        "us": 2.07,
        "ut": 2.17,
        "uu": 0.15,
        "uv": 0.26,
        "uw": 0.00,
        "ux": 0.07,
        "uy": 0.00,
        "uz": 0.24,
        "va": 3.36,
        "vb": 0.00,
        "vc": 0.01,
        "vd": 0.01,
        "ve": 4.75,
        "vf": 0.00,
        "vg": 0.00,
        "vh": 0.00,
        "vi": 3.19,
        "vj": 0.00,
        "vk": 0.00,
        "vl": 0.01,
        "vm": 0.01,
        "vn": 0.00,
        "vo": 1.75,
        "vp": 0.01,
        "vq": 0.00,
        "vr": 0.17,
        "vs": 0.01,
        "vt": 0.00,
        "vu": 0.07,
        "vv": 0.00,
        "vw": 0.00,
        "vx": 0.00,
        "vy": 0.00,
        "vz": 0.00,
        "wa": 0.11,
        "wb": 0.00,
        "wc": 0.00,
        "wd": 0.00,
        "we": 0.05,
        "wf": 0.00,
        "wg": 0.00,
        "wh": 0.01,
        "wi": 0.06,
        "wj": 0.00,
        "wk": 0.00,
        "wl": 0.00,
        "wm": 0.01,
        "wn": 0.04,
        "wo": 0.00,
        "wp": 0.00,
        "wq": 0.00,
        "wr": 0.01,
        "ws": 0.00,
        "wt": 0.00,
        "wu": 0.00,
        "wv": 0.00,
        "ww": 0.00,
        "wx": 0.00,
        "wy": 0.00,
        "wz": 0.00,
        "xa": 0.45,
        "xb": 0.00,
        "xc": 0.13,
        "xd": 0.01,
        "xe": 0.32,
        "xf": 0.00,
        "xg": 0.00,
        "xh": 0.00,
        "xi": 0.58,
        "xj": 0.00,
        "xk": 0.00,
        "xl": 0.00,
        "xm": 0.01,
        "xn": 0.00,
        "xo": 0.20,
        "xp": 0.42,
        "xq": 0.00,
        "xr": 0.00,
        "xs": 0.01,
        "xt": 0.24,
        "xu": 0.03,
        "xv": 0.01,
        "xw": 0.00,
        "xx": 0.01,
        "xy": 0.00,
        "xz": 0.00,
        "ya": 0.06,
        "yb": 0.01,
        "yc": 0.02,
        "yd": 0.02,
        "ye": 0.05,
        "yf": 0.01,
        "yg": 0.00,
        "yh": 0.00,
        "yi": 0.01,
        "yj": 0.00,
        "yk": 0.00,
        "yl": 0.02,
        "ym": 0.02,
        "yn": 0.02,
        "yo": 0.05,
        "yp": 0.01,
        "yq": 0.00,
        "yr": 0.01,
        "ys": 0.03,
        "yt": 0.01,
        "yu": 0.01,
        "yv": 0.00,
        "yw": 0.01,
        "yx": 0.00,
        "yy": 0.00,
        "yz": 0.00,
        "za": 1.20,
        "zb": 0.01,
        "zc": 0.05,
        "zd": 0.15,
        "ze": 0.86,
        "zf": 0.02,
        "zg": 0.00,
        "zh": 0.01,
        "zi": 0.29,
        "zj": 0.01,
        "zk": 0.00,
        "zl": 0.01,
        "zm": 0.08,
        "zn": 0.05,
        "zo": 0.33,
        "zp": 0.07,
        "zq": 0.08,
        "zr": 0.02,
        "zs": 0.05,
        "zt": 0.02,
        "zu": 0.06,
        "zv": 0.01,
        "zw": 0.00,
        "zx": 0.00,
        "zy": 0.02,
        "zz": 0.00,
    }
    return digrafos_pt


def analise_frequencia_colunar(cifrado):
    possiveis_chaves = list(permutations("abcd"))
    digrafos_pt = dict_digrafos()
    dict_possiveis_chaves = {}
    for (
        chave
    ) in possiveis_chaves:  # passa por cada chave possível no conjunto de 4 letras
        nova_chave = "".join(chave)
        dict_possiveis_chaves[nova_chave] = 0
        decripta_local = decripta_colunar(
            cifrado, nova_chave
        )  # gera o texto decifrado para aquela chave
        digrafos = acha_digrafos(decripta_local)
        for digrafo in digrafos:
            dict_possiveis_chaves[nova_chave] += digrafos_pt[
                digrafo
            ]  # adiciona a frequencia de cada dígrafo na chave correspondente
        trigrafos = acha_trigrafos(decripta_local)
        for trigrafo in trigrafos:
            if trigrafo in trigrafos_pt:
                dict_possiveis_chaves[nova_chave] += trigrafos_pt[trigrafo]
    chave_mais_provavel = max(
        dict_possiveis_chaves, key=dict_possiveis_chaves.get
    )  # pega a chave com maior frequencia de dígrafos
    print(f"A chave mais provável é: {chave_mais_provavel}")
    print(
        f"A mensagem decriptografada é: {decripta_colunar(cifrado, chave_mais_provavel)}"
    )
    num_trigrafos = 0
    for trigrafo in acha_trigrafos(decripta_colunar(cifrado, chave_mais_provavel)):
        num_trigrafos += 1


def grid():
    print("O que deseja fazer?")
    print("1 - Criptografar")
    print("2 - Decriptografar")
    print("3 - Força Bruta")
    print("4 - Análise de Frequência")
    print("5 - Sair")


grid()
escolha = input("Digite a opção desejada: ")
if escolha not in ["1", "2", "3", "4", "5"]:
    raise ValueError("Opção inválida")
escolha = int(escolha)
while escolha != 5:
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
    elif escolha == 4:
        print("Digite a mensagem cifrada:")
        mensagem = input()
        analise_frequencia_colunar(mensagem)
    grid()
    escolha = input()
    if not escolha in ["1", "2", "3", "4", "5"]:
        raise ValueError("Opção inválida")
    escolha = int(escolha)
