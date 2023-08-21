import pygame 
import random
from backend.modelo.jogador import *
from backend.geral.config import *

pygame.init()

pygame.display.set_caption("snake game")

#tamanho da tela
largura,altura = 600,400
fundo = pygame.display.set_mode((largura,altura))

#relogio
relogio = pygame.time.Clock()

#velocidade do jogo (frames)
velocidade_jogo = 8

#cores do jogo
preto = (0, 0, 0)
branca= (255, 255 ,255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

#parametros da snake
tamanho_quadrado = 10
velocidade_snake = 15

def gerar_comida(): 
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0 ) * 10.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(fundo, vermelha, [comida_x,comida_y, tamanho,tamanho])

def desenhar_cobra(tamanho,pixels):
    for pixel in pixels:
        pygame.draw.rect(fundo, verde, [pixel[0],pixel[1],tamanho,tamanho])

def desenhar_pontuacao(pontuacao):
    fonte= pygame.font.SysFont("Helvetica", 15)
    texto = fonte.render (f"Pontos: {pontuacao}", True, branca)
    fundo.blit(texto, [1,1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x=0
        velocidade_y=tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x=0
        velocidade_y=-tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x=tamanho_quadrado
        velocidade_y=0
    elif tecla == pygame.K_LEFT:
        velocidade_x=-tamanho_quadrado
        velocidade_y=0

    return velocidade_x, velocidade_y

def rodar():
    fim_jogo = False

    x = largura/2
    y = altura/2

    velocidade_x = 0
    velocidade_y = 0

    global tamanho_cobra
    tamanho_cobra = 1
    pixels = []

    comida_x , comida_y = gerar_comida()

    while not fim_jogo:
        fundo.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        #desenhar_comida            
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        #atualizar posição cobra
        if x < 0 or x >+ largura or y < 0 or y >+ altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y 

        #desenahr_cobra
        pixels.append([x,y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        #se a cobra bate em si
        for pixel in pixels [:-1]:
            if pixel == [x,y]:
                fim_jogo = True

        desenhar_cobra (tamanho_quadrado,pixels)

        #desenhar pontuação 
        desenhar_pontuacao(tamanho_cobra - 1)

        #atualizar a tela
        pygame.display.update()

        #criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra +=1
            comida_x, comida_y = gerar_comida()


        relogio.tick(velocidade_jogo)

rodar()

with app.app_context():
    j2 = Jogador(pontos = tamanho_cobra - 1 )
    db.session.add(j2)
    db.session.commit()
