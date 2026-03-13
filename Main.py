import Criaturas, Itens
import Personagem
from random import randrange

Personagem.iniAtr([8, 6, 4, 10])
Personagem.armadura = "A1"
nerd = Criaturas.Criatura()


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
                else:
                    ataque += (0, )
                Personagem.sofrerDano(ataque)
                if Personagem.vida[1] <= 0: break
            
            else:
                if "defesa" in Personagem.condicoes: Personagem.condicoes.remove("defesa")
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
                        ataque = Personagem.atacar(arma)
                        alvo = inivivo[(randrange(0, len(inivivo)))]
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
    
    else:
        print(f"{Personagem.nome}: {Personagem.vida[1]} pv", end="")
        [print(f"\t{i.nome}: {i.vida[1]} pv", end="") for i in inimigos]
        print("\n")
        if Personagem.vida[1] > 0:
            print(f"Parabéns, {Personagem.nome} venceu o combate!")
        else:
            print(f"infelizmente, {Personagem.nome} perdeu miseravelmente")

def mostraOpcoes(arma, armor):
    opt = None
    info = None

    

    return opt, info

combate(Criaturas.Criatura(), Criaturas.Criatura())
