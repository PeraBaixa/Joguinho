from random import randint

itens = []
class Item:
    def __init__(obj, nome="Moeda de 1 centavo", tipo="COLEC"):
        obj.nome = nome
        obj.tipo = tipo
        obj.id = "1"
        itens.append(obj)

def retornaColec(colec):
    match colec:
        case "1":
            return Item()

#Armas:
class Arma(Item):
    def __init__(obj, nome="Punhos", danoBase=1, pericia="Força", danoExtra=1):
        super().__init__(nome, "ARMA")
        obj.id = "W1" #W de weapon (vai ter que ser)
        obj.danoBase = danoBase
        obj.danoExtra = danoExtra
        obj.pericia = pericia
    
    def getDano(obj):
        
        return obj.danoBase + randint(0, obj.danoExtra)

class MachadoManeiro(Arma):
    def __init__(obj):
        super().__init__("Machado Maneiro", 3, "Força", 4)

class EscudoDeMesa(Arma):
    def __init__(obj):
        super().__init__("Escudo de Mesa", 1, "Resistência", 3)

class BolasMentais(Arma):
    def __init__(obj):
        super().__init__("Esferas de controle remoto", 1, "Concentração", 3)

class FacaNinja(Arma):
    def __init__(obj):
        super().__init__("Faca Ninja", 3, "Furtividade", 1)

class MarteloAssustador(Arma):
    def __init__(obj):
        super().__init__("Martelo Assustador", 2, "Intimidação", 2)

class Erro(Arma):#Arrumar essa arma:
    def __init__(obj):
        super().__init__("????", 0, "ENT", 2)

    def getDano(obj):
        return obj.danoBase    

def retornaArma(arma):
    match arma:
        case "W1":
            return Arma()

#Armaduras:
class Armadura(Item):
    def __init__(obj, nome="Jaqueta de couro"):
        super().__init__(nome, "ARMADURA")
        obj.id = "A1"
        obj.durab = 15
        obj.resis = 2

class Kevlar(Armadura):
    def __init__(obj):
        super().__init__("Kevlar")


def retornaArmadura(armor):
    match armor:
        case "A1":
            return Armadura()

#Utilitários:
class Util(Item):
    def __init__(obj, nome="Poção de vida"):
        super().__init__(nome, "UTIL")
        obj.id = "U1"
    
    def efeito(obj):
        return [[4, "VID"]]

class PotFisi(Util):
    def __init__(obj):
        super().__init__("Poção de poder físico")
        obj.id = "U2"
    
    def efeito(obj):
        return [[2, "COR"], [1, "AGI"]]

class PotMente(Util):
    def __init__(obj):
        super().__init__("Poção de poder mental")
        obj.id = "U3"
    
    def efeito(obj):
        return [[2, "MEN"], [1, "VON"]]

def retornaUtil(util):
    match util:
        case "U1":
            return Util()
        case "U2":
            return PotFisi()
        case "U3":
            return PotMente()
    
def retornaItem(item):
    match item[0]:
        case "W":
            retornaArma(item)
        case "A":
            retornaArmadura(item)
        case "U":
            retornaItem(item)
        case __:
            retornaColec(item)