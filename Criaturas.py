from random import randint

criaturas = []
class Criatura:
    def __init__(obj):
        #Os 3 elementos da lista VIDA representam, respectivamente:
        #vida máxima, vida atual e vida temporária
        obj.vida = [10, 10, 0]

        obj.atrs = {
            "COR": 4,
            "AGI": 3,
            "MEN": 8,
            "VON": 3
        }
        obj.mult = {
            "COR": 1,
            "AGI": 1,
            "MEN": 1,
            "VON": 1
        }
        obj.entro = 9

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
    
    def atacar(obj):
        #Ataque de garras
        dano = randint(0, 2)
        crit = False

        if randint(1, 100) <= (20*obj.getBon("VON")):
            print("CRITICO!")
            crit = True
            dano*=2

        return (dano, crit, obj.getBon("MEN"))

    def sofrerDano(obj, info):
        danofin = info[0]
        desviar = obj.getBon("AGI")*10
        porcMax = 100 + (info[2]*10)

        if randint(1, porcMax) > desviar or info[1]:
            if obj.vida[2] > 0:
                danofin -= obj.vida[2]
                obj.vida[2] -= info[0]
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