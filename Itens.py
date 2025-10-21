from Classesgen import Item, Util, Arma, Armadura

#Utilitários:
class PotFisi(Util):
    def __init__(obj):
        super().__init__("Poção de poder físico")
    
    def efeito(obj):
        return [[2, "COR"], [1, "AGI"]]

class PotMente(Util):
    def __init__(obj):
        super().__init__("Poção de poder mental")
    
    def efeito(obj):
        return [[2, "MEN"], [1, "VON"]]


#Armas
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

#Arrumar essa arma:
class Erro(Arma):
    def __init__(obj):
        super().__init__("????", 0, "ENT", 2)

    def getDano(obj)
        return obj.danoBase

#Armaduras
class Kevlar(Armadura):
    def __init__(obj):
        super().__init__("Kevlar")
