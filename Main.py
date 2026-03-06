import Criaturas, Itens
import Personagem

Personagem.iniAtr([8, 6, 4, 4])
nerd = Criaturas.Criatura()


def criaOrdem(protag=False, *ini):
    ordem = [ini[0]]
    for mon in ini[1:]:
        for i, o in enumerate(ordem):
            if o.atrs["AGI"] <= mon.atrs["AGI"]:
                ordem.insert(i, mon)
                break
        else:
            ordem.append(mon.cod)

    if protag:
        for i, ini in enumerate(ordem):
            if Personagem.atrs["AGI"] >= ini.atrs["AGI"]:
                ordem.insert(i, 0)
                break
        else:
            ordem.append(0)
    
    return ordem

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
    else: print(f"{nerd.nome} com {nerd.vida[1]} de pv")
