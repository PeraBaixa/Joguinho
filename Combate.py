import Criaturas, Itens
import Personagem as P
from random import randrange

INIMIGO = Criaturas.Criatura()

def atacar(prot=True):
    if INIMIGO == None: return
    log = []
    cond = None

    nome = (P.nome if prot else INIMIGO.nome)
    nomeIni = (INIMIGO.nome if prot else P.nome)
    ataque = (P.atacar(Itens.retornaItem(P.arma)) if prot else INIMIGO.atacar())

    return ("atk", ataque)
    if "defesa" in (INIMIGO.condicoes if prot else P.condicoes):
        if prot:
            ataque += (INIMIGO.defender(), )
            INIMIGO.condicoes.remove("defesa")

        else:
            ataque += ((Itens.retornaItem(P.armadura).getResis() if P.armadura else 0), )
            P.condicoes.remove("defesa")
    else:
        ataque += (0, )

    cond = (INIMIGO.sofrerDano(ataque) if prot else P.sofrerDano(ataque))

    log.append(f"{nome} ataca")
    
    if cond:
        if ataque[1]: log.append("Acerto crítico!")
        log.append(f"{nomeIni} recebeu {ataque[0]+ataque[1]} pontos de dano")
    else:
        log.append(f"{nomeIni} desviou!")
    
    return log

def defender(prot):
    if not INIMIGO: return

    cond = (P.condicoes if prot else INIMIGO.condicoes)
    cond.append("defesa")
    return "def"
    return [f"{P.nome if prot else INIMIGO.nome} se defende!"]
    

def iniEscolha():
    match INIMIGO.definirEscolha():
        case "atk":
            return atacar(False)
        case "def":
            return defender(False)
        case __:
            return [f"{INIMIGO.nome} não faz nada"]
        
def interagir(protAcao, iniAcao):
    log = []
    if protAcao[0] == "def": log.append(f"{P.nome} se defende!")     
    if iniAcao[0] == "def": log.append(f"{INIMIGO.nome} se defende!")

    if protAcao[0] == "atk":
        if INIMIGO.sofrerDano(protAcao[1]): log.append(f"{INIMIGO.nome} sofreu {protAcao[1][0]+protAcao[1][1]} pontos de dano")
        else: log.append(f"{INIMIGO.nome} desviou!")
    if iniAcao[0] == "atk":
        if P.sofrerDano(iniAcao[1]): log.append(f"{P.nome} sofreu {iniAcao[1][0]+iniAcao[1][1]} pontos de dano")
        else: log.append(f"{P.nome} desviou!")
    

"""
def criaOrdem(ini):
    ordem = [ini[0]]
    for mon in ini[1:]:
        for i, o in enumerate(ordem):
            if o.atrs["AGI"] <= mon.atrs["AGI"]:
                ordem.insert(i, mon)
                break
        else:
            ordem.append(mon)
    
    #Adiciona o protagonista à ordem:
    for i, op in enumerate(ordem):
        if Personagem.atrs["AGI"] >= op.atrs["AGI"]:
            ordem.insert(i, 0)
            break
    else:
        ordem.append(0)
    
    return ordem

#Função provisória para criar combate
def combate(*inimigos):
    inivivo = list(inimigos)
    ataque, defesa = None, None
    arma = Itens.retornaItem(Personagem.arma)
    armadura = Itens.retornaItem(Personagem.armadura) 

    while Personagem.vida[1] > 0 and len(inivivo) > 0:
        print(f"{Personagem.nome}: {Personagem.vida[1]} pv", end="")
        [print(f"\t{i.nome}: {i.vida[1]} pv", end="") for i in inimigos]
        print()

        for ini in criaOrdem(inivivo):
            if ini:
                ataque = ini.atacar()
                print(f"{ini.nome} ataca, dando {ataque[0]} de dano")
                if "defesa" in Personagem.condicoes and armadura:
                    ataque += (armadura.getResis(), )
                    Personagem.condicoes.remove("defesa")
                else:
                    ataque += (0, )
                Personagem.sofrerDano(ataque)
                if Personagem.vida[1] <= 0: break
            #Vez do personagem
            else:
                print(f"Sua vez, {Personagem.nome}!")
                print("1 - Atacar")
                print("2 - Defender")
                try:
                    opt = int(input("Decida sua ação: "))
                except:
                    opt = None

                match opt:
                    #Atacar
                    case 1:
                        if len(inivivo) > 1:
                            [print(f"{n+1} - {i.nome}") for n,i in enumerate(inivivo)]
                            try:
                                alvo = inivivo[int(input("Escolha qual inimigo atacar: "))-1]
                            except:
                                alvo = inivivo[0]
                        else:
                            alvo = inivivo[0]
                        ataque = Personagem.atacar(arma)
                        print(f"{Personagem.nome} ataca, dando {ataque[0]+ataque[1]} de dano")
                        alvo.sofrerDano(ataque)
                        if alvo.vida[1] <= 0: inivivo.remove(alvo)
                        if len(inivivo) <= 0: break
                    #Defender
                    case 2:
                        print(f"{Personagem.nome} se defende!")
                        Personagem.condicoes.append("defesa")
                    #Fugir
                    case __:
                        pass
        print()
    
    else:
        print(f"{Personagem.nome}: {Personagem.vida[1]} pv", end="")
        [print(f"\t{i.nome}: {i.vida[1]} pv", end="") for i in inimigos]
        print()
        if Personagem.vida[1] > 0:
            print(f"Parabéns, {Personagem.nome} venceu o combate!")
        else:
            print(f"infelizmente, {Personagem.nome} perdeu miseravelmente")
        
"""