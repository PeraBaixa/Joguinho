from turtle import Screen
import pygame
from random import randrange
import os

from Combate import *
from Personagem import vida, nome

pygame.init()
pygame.display.set_caption("Hora da Escola")

#Constantes gerais
LARGURA, ALTURA = 800, 600
FPS = 60
TELA = pygame.display.set_mode((LARGURA, ALTURA))
CLOCK = pygame.time.Clock()

#Constantes de cores:
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (128, 128, 128)
AZUL = (0, 0, 255)
CIANO = (0, 255, 255)
VERDE = (0, 255, 0) #Mais especificamente, verde-limão
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
LARANJA = (255, 165, 0)
ROXO = (128, 0, 128)

FONTEBOTAO = pygame.font.Font(None, 40)
BOTAORECT = pygame.Rect(10, 480, 385, 50) #Tamanho padrão de um botão

class Botao:
    def __init__(obj, texto, acao, loc=None, corT=BRANCO):
        obj.texto = FONTEBOTAO.render(texto, True, corT)
        obj.dimen = BOTAORECT.copy()
        if loc: obj.dimen.topleft = loc
        obj.acao = acao
        obj.cor = PRETO
        obj.clicado = False

    def verificaClique(obj, mPos):
        x, y = mPos
        checkX = (obj.dimen.x <= x <= (obj.dimen.x + obj.dimen.width))
        checkY = (obj.dimen.y <= y <= (obj.dimen.y + obj.dimen.height))

        if checkX and checkY and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
    
    def verificaSobre(obj, mPos):
        x, y = mPos
        checkX = (obj.dimen.x <= x <= (obj.dimen.x + obj.dimen.width))
        checkY = (obj.dimen.y <= y <= (obj.dimen.y + obj.dimen.height))

        if (checkX and checkY):
            obj.cor = CINZA
        else: 
            obj.cor = PRETO

    def desenhar(obj):
        rect = obj.dimen
        pygame.draw.rect(TELA, BRANCO, rect)
        pygame.draw.rect(TELA, obj.cor, pygame.Rect((rect.x+2), (rect.y+2), rect.width-4, rect.height-4))
        TELA.blit(obj.texto, obj.texto.get_rect(center=obj.dimen.center))

def testa():
    print("Teste")

def movimentar(tecla, loc):
    if tecla[pygame.K_a] and (loc.x - 5) >= 0:
        loc.x -= 5
    if tecla[pygame.K_d] and (loc.x + 5) <= (LARGURA - 100):
        loc.x += 5
    if tecla[pygame.K_w] and (loc.y - 5) >= 0:
        loc.y -= 5
    if tecla[pygame.K_s] and (loc.y + 5) <= (ALTURA - 200):
        loc.y += 5

def carrega_imagem(arq, tam):
    if os.path.exists(arq):
        img = pygame.image.load(arq).convert_alpha()
        img = pygame.transform.scale(img, tam)
    else:
        img = pygame.Surface(tam)
        img.fill((255, 255, 255))
    
    return img

def main():
    nerd = carrega_imagem("Sprites/Amigo nerd (zumbi).png", (360, 410))
    jogador = carrega_imagem("Sprites/Protagonista.png", (360, 410))
    vidaFonte = pygame.font.Font(None, 25)
    nomes = [
        vidaFonte.render(P.nome, True, BRANCO),
        vidaFonte.render(INIMIGO.nome, True, BRANCO)
    ]

    vidaMax = 140

    menuComb = []
    menuComb.append(Botao("Atacar", atacar))
    menuComb.append(Botao("Defender", testa, loc=(405, 480)))
    menuComb.append(Botao("Itens", testa, loc=(10, 540)))
    menuComb.append(Botao("Fugir", testa, loc=(405, 540)))

    display = [menuComb, None, 0]

    while True:
        CLOCK.tick(FPS)
        TELA.fill(CIANO)
        
        mPos = pygame.mouse.get_pos()
        teclas = pygame.key.get_pressed()
        #movimentar(teclas, jogloc)        
        TELA.blit(jogador, (50, 80))
        TELA.blit(nomes[0], (50, 50))
        pygame.draw.rect(TELA, BRANCO, ((nomes[0].get_rect(topleft=(50, 50)).right + 5), 45, (vidaMax+4), 25))
        pygame.draw.rect(TELA, PRETO, ((nomes[0].get_rect(topleft=(50, 50)).right + 7), 47,vidaMax, 21))
        pygame.draw.rect(TELA, VERDE, ((nomes[0].get_rect(topleft=(50, 50)).right + 7), 47, (vidaMax*vida["atual"]/vida["max"]), 21))

        TELA.blit(nerd, (450, 50))
        TELA.blit(nomes[1], (450, 50))
        pygame.draw.rect(TELA, BRANCO, ((nomes[1].get_rect(topleft=(450, 50)).right + 5), 45, (vidaMax+4), 25))
        pygame.draw.rect(TELA, PRETO, ((nomes[1].get_rect(topleft=(450, 50)).right + 7), 47, vidaMax, 21))
        pygame.draw.rect(TELA, VERDE, ((nomes[1].get_rect(topleft=(450, 50)).right + 7), 47, (vidaMax*INIMIGO.vida["atual"]/INIMIGO.vida["max"]), 21))

        if not display[1]:
            for botao in display[0]:
                botao.verificaSobre(mPos)
                botao.desenhar()
                if botao.verificaClique(mPos):
                    protLog = botao.acao()
                    iniLog = iniEscolha()
                    display[1] = (protLog())
                    pygame.time.wait(300)
        else:
            pygame.draw.rect(TELA, BRANCO, (10, 480, 780, 110))
            pygame.draw.rect(TELA, PRETO, (12, 482, 776, 106))
            TELA.blit(FONTEBOTAO.render(display[1][display[2]], True, BRANCO), (16, 486))
            if pygame.mouse.get_pressed()[0]:
                display[2] += 1
                if display[2] > (len(display[1]) - 1):
                    display[1] = None
                    display[2] = 0
                pygame.time.wait(300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or teclas[pygame.K_ESCAPE]:
                pygame.quit()
                return
        
        pygame.display.flip()

if __name__ == "__main__":
    main()