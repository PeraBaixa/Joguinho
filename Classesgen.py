from random import randint

criaturas, itens = [], []

class Criatura:
    def __init__(obj):
        #Os 3 elementos da lista VIDA representam, respectivamente:
        #vida máxima, vida atual e vida temporária
        obj.vida = [10, 10, 0]

        obj.atrs = {
            "COR": 4,
            "AGI": 6,
            "MEN": 3,
            "VON": 3
        }
        obj.mult = {
            "COR": 1,
            "AGI": 1,
            "MEN": 1,
            "VON": 1
        }
        obj.pericias = [
            {"nome": "Força", "bon": 0, "atrbase": "COR"},
            {"nome": "Resistência", "bon": 0, "atrbase": "COR"},
            {"nome": "Furtividade", "bon": 0, "atrbase": "AGI"},
            {"nome": "Precisão", "bon": 0, "atrbase": "AGI"},
            {"nome": "Percepção", "bon": 0, "atrbase": "MEN"},
            {"nome": "Memória", "bon": 0, "atrbase": "MEN"},
            {"nome": "Concentração", "bon": 0, "atrbase": "VON"},
            {"nome": "Intimidação", "bon": 0, "atrbase": "VON"}
        ]

        obj.cod = (criaturas[-1].cod + 1 if len(criaturas) > 0 else 1)
        criaturas.append(obj)
 
        obj.ataVel = 1
        #1 de AGI = 0.25
        #2, 3 de AGI = 0.33
        #4, 5 de AGI = 0.5
        #6, 7 de AGI = 1
        #8, 9 de AGI = 2
        #10 de AGI = 3
        obj.condicoes = []
    
    def getBon(obj, atr):
        match atr.upper():
            case "COR"|"AGI"|"MEN"|"VON":
                return (obj.atrs[atr]*obj.mult[atr])-5
            case "ENT":
                return (obj.entro)-5
            case __:
                return 0
            
    def bonPericia(obj, pericia):
        for per in obj.pericias:
            if per["nome"] == pericia:
                bonus = obj.getBon(per["atrbase"])
                return per["bon"] + bonus

        return 0
    
    def atacar(obj):
        #Ataque de garras
        dano = obj.bonPericia("Precisão") + randint(0, 2)
        if randint(1, 100) <= (20*obj.getBon("VON")):
            print("CRITICO!")
            dano*=2

        return dano

    def sofrerDano(obj, dano, intIni):
        danofin = dano
        desviar = obj.getBon("MEN")*10
        porcMax = 100 + (intIni*10)

        if randint(1, porcMax) > desviar:
            if obj.vida[2] > 0:
                danofin -= obj.vida[2]
                obj.vida[2] -= dano
                if danofin < 0: danofin = 0
                if obj.vida[2] < 0: obj.vida[2] = 0 
            
            obj.vida[1] -= danofin
        else:
            print("O monstro desviou!")

    @staticmethod
    def achaCriatura(cri):
        for c in criaturas:
            if c.cod == cri:
                return c
        else:
            return 0

class Item:
    def __init__(obj, nome="Moeda de 1 centavo", tipo="COLEC"):
        obj.nome = nome
        obj.tipo = tipo
        obj.qunt = 1
        obj.cod = (itens[-1].cod + 1 if len(itens) > 0 else 1)
        itens.append(obj)

    @staticmethod
    def achaItem(item):
        for i in itens:
            if i.cod == item:
                return i
        else:
            return 0

class Arma(Item):
    def __init__(obj, nome="Punhos", danoBase=1, pericia="Força", danoExtra=1):
        super().__init__(nome, "ARMA")
        obj.danoBase = danoBase
        obj.danoExtra = danoExtra
        obj.pericia = pericia
    
    def getDano(obj):
        
        return obj.danoBase + randint(0, obj.danoExtra)

class Armadura(Item):
    def __init__(obj, nome="Jaqueta de couro"):
        super().__init__(nome, "ARMADURA")
        obj.durab = 15
        obj.resis = 2

class Util(Item):
    def __init__(obj, nome="Poção de vida"):
        super().__init__(nome, "UTIL")
    
    def efeito(obj):
        return [[4, "VID"]]