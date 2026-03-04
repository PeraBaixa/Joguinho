import Criaturas, Itens
import Personagem

achaCriatura = Criaturas.achaCriatura
achaItem = Itens.Item.achaItem

Personagem.iniAtr([8, 6, 4, 4])
nerd = Criaturas.Criatura()


def criaOrdem(protag=False, *pers):
    ordem = [pers[0].cod]
    for p in pers[1:]:
        for i, o in enumerate(ordem):
            if achaCriatura(o).atrs["AGI"] <= p.atrs["AGI"]:
                ordem.insert(i, p.cod)
                break
        else:
            ordem.append(p.cod)

    if protag:
        for i, c in enumerate(ordem):
            if Personagem.atrs["AGI"] >= achaCriatura(c).atrs["AGI"]:
                ordem.insert(i, 0)
                break
        else:
            ordem.append(0)
    
    return ordem

#Simulação de combate simples:
while nerd.vida[1] > 0 and Personagem.vida[1] > 0:
    print(f"{Personagem.nome}: {Personagem.vida[1]} pv\tMonstro: {nerd.vida[1]} pv")
    for p in criaOrdem(True, nerd):
        ataque = 0
        if p == 0:
            ataque = Personagem.atacar()
            print(f"{Personagem.nome} ataca, dando {ataque} de dano")
            nerd.sofrerDano(ataque, Personagem.getBon("MEN"))
            if nerd.vida[1] <= 0:
                break
        else:
            ataque = nerd.atacar()
            print(f"O monstro ataca, dando {ataque} de dano")
            Personagem.sofrerDano(ataque, nerd.getBon("MEN"))
            if Personagem.vida[1] <= 0:
                break
else:
    print(f"{Personagem.nome}: {Personagem.vida[1]} pv\tMonstro: {nerd.vida[1]} pv")
    print(f"Vencedor: {f"{Personagem.nome} com {Personagem.vida[1]} de pv" if nerd.vida[1] <= 0 else f"o monstro com {nerd.vida[1]}"}")