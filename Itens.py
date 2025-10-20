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