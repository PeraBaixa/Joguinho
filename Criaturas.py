from random import randint

criaturas = []
class Criatura:
    def __init__(obj):
        obj.nome = "Amigo nerd"
        #Os 3 elementos da lista VIDA representam, respectivamente:
        #vida atual, vida máxima e vida temporária
        obj.vida = {
            "atual":10,
            "max": 10,
            "escudo": 0
        }

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
        obj.defesa = 1

        obj.cod = (criaturas[-1].cod + 1 if len(criaturas) > 0 else 1)
        criaturas.append(obj)
        
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
        crit = 0

        if randint(1, 100) <= (20*obj.getBon("VON")):
            print("CRITICO!")
            crit = dano

        return (dano, crit, obj.getBon("MEN"))

    def defender(obj):
        return 2

    def definirEscolha(obj):
        chance = randint(1, 100)

        if chance == 1:
            return None
        elif chance < 30:
            return "def"
        else:
            return "atk"

    def sofrerDano(obj, info):
        danofin = info[0]+info[1]
        desviar = obj.getBon("AGI")*10
        porcMax = 100 + (info[2]*10)

        if randint(1, porcMax) > desviar:
            if obj.vida["escudo"] > 0:
                danofin -= obj.vida["escudo"]
                obj.vida["escudo"] -= (info[0]+info[1])
                if danofin < 0: danofin = 0
                if obj.vida["escudo"] < 0: obj.vida[2] = 0

            if "defesa" in obj.condicoes:
                danofin =- obj.defesa
                obj.condicoes.remove("defesa")
                if danofin < 0: danofin = 0
            
            obj.vida["atual"] -= danofin
            return True
        else:
            return False

    @staticmethod
    def achaCriatura(cri):
        for c in criaturas:
            if c.cod == cri:
                return c
        else:
            return 0
