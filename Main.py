import Criaturas, Itens
import Personagem
from random import randrange

Personagem.iniAtr([8, 6, 4, 10])
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

    while Personagem.vida[1] > 0 and len(inivivo) > 0:
        print(f"{Personagem.nome}: {Personagem.vida[1]} pv", end="")
        [print(f"\t{i.nome}: {i.vida[1]} pv", end="") for i in inimigos]
        print()

        for p in criaOrdem(inivivo):
            if p:
                ataque = p.atacar()
                print(f"{p.nome} ataca, dando {ataque[0]} de dano")
                Personagem.sofrerDano(ataque)
                if Personagem.vida[1] <= 0: break
            
            else:
                ataque = Personagem.atacar(arma)
                alvo = inivivo[(randrange(0, len(inivivo)))]
                print(f"{Personagem.nome} ataca, dando {ataque[0]} de dano")
                alvo.sofrerDano(ataque)
                if alvo.vida[1] <= 0: inivivo.remove(alvo)
                if len(inivivo) <= 0: break
    else:
        print(f"{Personagem.nome}: {Personagem.vida[1]} pv", end="")
        [print(f"\t{i.nome}: {i.vida[1]} pv", end="") for i in inimigos]
        print("\n")
        if Personagem.vida[1] > 0:
            print(f"Parabéns, {Personagem.nome} venceu o combate!")
        else:
            print(f"infelizmente, {Personagem.nome} perdeu miseravelmente")

combate(Criaturas.Criatura(), Criaturas.Criatura())

"""
#Simulação de combate simples:
while nerd.vida[1] > 0 and Personagem.vida[1] > 0:
    print(f"{Personagem.nome}: {Personagem.vida[1]} pv\tMonstro: {nerd.vida[1]} pv")
    for p in criaOrdem(True, nerd):
        ataque = None
        if p == 0:
            ataque = Personagem.atacar(Itens.retornaItem(Personagem.arma))
            print(f"{Personagem.nome} ataca, dando {ataque[0]} de dano")
            nerd.sofrerDano(ataque)
            if nerd.vida[1] <= 0:
                break
        else:
            ataque = nerd.atacar()
            print(f"{nerd.nome} ataca, dando {ataque[0]} de dano")
            Personagem.sofrerDano(ataque)
            if Personagem.vida[1] <= 0:
                break
else:
    print(f"{Personagem.nome}: {Personagem.vida[1]} pv\tMonstro: {nerd.vida[1]} pv")
    print("Vencedor:")
    if nerd.vida[1] > 0: print(f"{Personagem.nome} com {Personagem.vida[1]} de pv") 
    else: print(f"{nerd.nome} com {nerd.vida[1]} de pv")"""
