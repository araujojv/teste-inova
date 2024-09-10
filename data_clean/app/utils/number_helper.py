unidades = {
    "zero": 0,
    "um": 1,
    "dois": 2,
    "três": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
}

dezenas = {
    "dez": 10,
    "vinte": 20,
    "trinta": 30,
    "quarenta": 40,
    "cinquenta": 50,
    "sessenta": 60,
    "setenta": 70,
    "oitenta": 80,
    "noventa": 90,
}

especiais = {
    "onze": 11,
    "doze": 12,
    "treze": 13,
    "quatorze": 14,
    "quinze": 15,
    "dezesseis": 16,
    "dezessete": 17,
    "dezoito": 18,
    "dezenove": 19,
}

centenas = {
    "cem": 100,
    "cento": 100,
    "duzentos": 200,
    "trezentos": 300,
    "quatrocentos": 400,
    "quinhentos": 500,
    "seiscentos": 600,
    "setecentos": 700,
    "oitocentos": 800,
    "novecentos": 900,
}

milhares = {"mil": 1000}


def extenso_para_numero(palavra):
    palavra = palavra.strip().lower()

    if palavra in especiais:
        return especiais[palavra]

    if palavra in unidades:
        return unidades[palavra]

    if palavra in dezenas:
        return dezenas[palavra]

    if palavra in centenas:
        return centenas[palavra]

    if palavra in milhares:
        return milhares[palavra]

    partes = palavra.split(" e ")
    if len(partes) == 2:
        if partes[0] in dezenas and partes[1] in unidades:
            return dezenas[partes[0]] + unidades[partes[1]]
        if partes[0] in centenas and partes[1] in dezenas:
            return centenas[partes[0]] + dezenas[partes[1]]

    if "mil" in palavra:
        partes_milhar = palavra.split(" mil")
        if len(partes_milhar) == 2:
            milhar = partes_milhar[0].strip()
            if milhar in unidades:
                return unidades[milhar] * 1000

    return None


def apenas_numeros(s):
    return "".join(char for char in s if char.isdigit())
