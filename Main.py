from turtle import Screen
import pygame
from random import randrange
import os

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
    def __init__(obj, texto, acao, loc=None, corB=BRANCO, corT=PRETO):
        obj.texto = FONTEBOTAO.render(texto, True, corT)
        obj.dimen = BOTAORECT.copy()
        if loc: obj.dimen.topleft = loc
        obj.acao = acao
        obj.cor = corB
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

        return (checkX and checkY)

    def desenhar(obj):
        pygame.draw.rect(TELA, obj.cor, obj.dimen)
        TELA.blit(obj.texto, obj.texto.get_rect(center=obj.dimen.center))

def testa():
    print("Teste")

def carrega_imagem(arq, tam):
    if os.path.exists(arq):
        img = pygame.image.load(arq).convert_alpha()
        img = pygame.transform.scale(img, tam)
    else:
        img = pygame.Surface(tam)
        img.fill((255, 255, 255))
    
    return img

def movimenta(tecla, loc):
    if tecla[pygame.K_a] and (loc.x - 5) >= 0:
        loc.x -= 5
    if tecla[pygame.K_d] and (loc.x + 5) <= (LARGURA - 100):
        loc.x += 5
    if tecla[pygame.K_w] and (loc.y - 5) >= 0:
        loc.y -= 5
    if tecla[pygame.K_s] and (loc.y + 5) <= (ALTURA - 200):
        loc.y += 5

def main():
    jogador = carrega_imagem("Sprites/Protagonista.png", (200, 250))
    jogloc = jogador.get_rect()
    menuComb = []
    menuComb.append(Botao("Atacar", testa))
    menuComb.append(Botao("Defender", testa, loc=(405, 480)))
    menuComb.append(Botao("Itens", testa, loc=(10, 540)))
    menuComb.append(Botao("Fugir", testa, loc=(405, 540)))

    while True:
        CLOCK.tick(FPS)
        TELA.fill((0, 0, 0))
        
        mPos = pygame.mouse.get_pos()
        teclas = pygame.key.get_pressed()
        movimenta(teclas, jogloc)

        for botao in menuComb:
            if botao.verificaSobre(mPos):
                botao.cor = CINZA
            else:
                botao.cor = BRANCO
            botao.desenhar()
            if botao.verificaClique(mPos):
                botao.acao()
                pygame.time.wait(300)

        
        TELA.blit(jogador, jogloc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or teclas[pygame.K_ESCAPE]:
                pygame.quit()
                return
        
        pygame.display.flip()

if __name__ == "__main__":
    main()