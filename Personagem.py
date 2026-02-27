from random import randint

nome = "Carlos"
#Os 3 elementos da lista VIDA representam, respectivamente:
#vida máxima, vida atual e vida temporária
vida = [10, 10, 0]

atrs = {
    "COR": 5,
    "AGI": 5,
    "MEN": 5,
    "VON": 5
}
bonusTemp = {
    "COR": 0,
    "AGI": 0,
    "MEN": 0,
    "VON": 0
}
mult = {
    "COR": 1,
    "AGI": 1,
    "MEN": 1,
    "VON": 1
}
entro = 8
pericias = [
    {"nome": "Destruir", "bon": 0, "atrbase": "COR"},
    {"nome": "Resistência", "bon": 0, "atrbase": "COR"},
    {"nome": "Esconder", "bon": 0, "atrbase": "AGI"},
    {"nome": "Arremessar", "bon": 0, "atrbase": "AGI"},
    {"nome": "Encontrar", "bon": 0, "atrbase": "MEN"},
    {"nome": "Curar", "bon": 0, "atrbase": "MEN"},
    {"nome": "Resistir", "bon": 0, "atrbase": "VON"},
    {"nome": "Comunicar", "bon": 0, "atrbase": "VON"}
]

ataVel = 1
condicoes = []
inventario = [("1", 1), ("W1", 1)]

arma = "W1" #A arma equipada inicial são os Punhos do Jogador
armadura = None

#Muda a quantidade de itens no inventario
def interItem(item, qunt=1):
    for i, it in enumerate(inventario):
        if it[0] == item:
            it[1] += qunt
            if it[0] < 1: del inventario[i]
            break
    else:
        if qunt > 0:
            inventario.append((item, qunt))

def receberEfeito(origem, code):#Os parâmetros são o código do item e a lista de códigos que vieram do efeito do utilitário
    for efeito in code():
        match efeito[1]:
            case "VID":
                vida[1] += efeito[1]
                if vida[1] > vida[0]: vida[1] = vida[0]

            case "COR"|"AGI"|"MEN"|"VON":
                bonusTemp[efeito[1]] += efeito[0]
    
    interItem(origem, -1)

def listInven():
    return [f"{Item.achaItem(i).qunt} | {Item.achaItem(i).nome}" for i in inventario]

def getBon(atr):
    match atr.upper():
        case "COR"|"AGI"|"MEN"|"VON":
            return ((atrs[atr]*mult[atr])-5)+ bonusTemp[atr]
        case "ENT":
            return (entro)-5
        case __:
            return 0

def bonPericia(pericia):
    for per in pericias:
        if per["nome"] == pericia:
            bonus = getBon(per["atrbase"])

            return per["bon"] + bonus

    return 0

def atacar(arma):
    dano = (arma.getDano() + bonPericia(arma.pericia))
    crit = False

    if randint(1, 100) <= (20*getBon("VON")):
        print("CRITICO!")
        crit = True
        dano*=2

    return (dano, crit, getBon("MEN"))

def sofrerDano(info):
    desviar = getBon("AGI")*10
    porcMax = 100 + (info[2]*10)
    danofin = info[0]

    if randint(1, porcMax) > desviar or info[1]:
        if vida[2] > 0:
            danofin -= vida[2]
            vida[2] -= info[0]
            if danofin < 0: danofin = 0
            if vida[2] < 0: vida[2] = 0
        
        vida[1] -= danofin
    else:
        print(nome + " desviou!")

def iniAtr(ats):
    global ataVel

    atrs["COR"] = ats[0]
    atrs["AGI"] = ats[1]
    atrs["MEN"] = ats[2]
    atrs["VON"] = ats[3]

    vida[0] = atrs["COR"]*2
    vida[1] = atrs["COR"]*2

    match atrs["AGI"]:
        case 1:
            ataVel = 4
        case 2|3:
            ataVel = 3
        case 4|5:
            ataVel = 2
        case 6|7:
            ataVel = 1
        case 8:
            ataVel = 0.5

def adiAtr(aum, atr):
    global ataVel

    if atrs[atr] + aum > 10:
        atrs[atr] = 10
    else:
        atrs[atr] += aum

    if atr == "COR":
        if aum > 0:
            vida[0] += 2*aum
            vida[1] += 2*aum
    if atr == "AGI":
        match (atrs["AGI"]*mult["AGI"]):
            case 1:
                ataVel = 0.25
            case 2|3:
                ataVel = 0.4
            case 4|5:
                ataVel = 0.5
            case 6|7:
                ataVel = 1
            case 8|9:
                ataVel = 0.5
            case 10:
                ataVel = 0.3
            case __:
                ataVel = 0.25