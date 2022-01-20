#
# dopo aver eseguito il programa si puù iniziare subito a giocare
#
# la macchina arancione verrà controllata dal tasto Q
#
# la macchina azzurra verrà controllata dal tasto R
#
# la macchina rossa verrà controllata dal tasto U
#
# la macchina verde verrà controllata dal tasto P
#
#
# per vincere bisogna premere più volte velocemente il proprio pulsante
#
# premi spazio per iniziare la gara successiva
#
# vince chi arriva a 3 gare vinte!
#

from pygame.locals import *
import pygame

pygame.init()

arancio=pygame.image.load("arancio.png")
azzurra=pygame.image.load("azzurra.png")
rossa=pygame.image.load("rossa.png")
verde=pygame.image.load("verde.png")
strada=pygame.image.load("strada.png")
vinto=pygame.image.load("ha_vinto_text.png")
coppa=pygame.image.load("coppa.png")
winner_text=pygame.image.load("winner_text.png")
spazio=pygame.image.load("spazio_text.png")
screen = pygame.display.set_mode((1000, 720))
clock = pygame.time.Clock()

def inizzializza():
    global x_arancio, x_azzurra, x_rossa, x_verde
    x_arancio, x_azzurra, x_rossa, x_verde = 0, 0, 0, 0
    screen.blit(strada, (0,0))
    screen.blit(arancio, (0,40))
    screen.blit(azzurra, (0,220))
    screen.blit(rossa, (0,400))
    screen.blit(verde, (0,580))

def aggiorna():
    screen.blit(strada, (0,0))
    screen.blit(arancio, (x_arancio,40))
    screen.blit(azzurra, (x_azzurra,220))
    screen.blit(rossa, (x_rossa,400))
    screen.blit(verde, (x_verde,580))

def vittoria(colore):
    global arancio_win, azzurra_win, rossa_win, verde_win
    if colore == 'arancio':
        coords = (20,55)
        if arancio_win == 3:
            gameover('arancio')
    elif colore == 'azzurra':
        coords = (20,235)
        if azzurra_win == 3:
            gameover('azzurra')
    elif colore == 'rossa':
        coords = (20,415)
        if rossa_win == 3:
            gameover('rossa')
    elif colore == 'verde':
        coords = (20,595)
        if verde_win == 3:
            gameover('verde')
    screen.blit(vinto, coords)
    pygame.display.update()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = False
            screen.blit(spazio, (401,700))
            clock.tick(60)
            pygame.display.update()
    inizzializza()

def gameover(colore):
    if colore == 'arancio':
        winner = arancio
    elif colore == 'azzurra':
        winner = azzurra
    elif colore == 'rossa':
        winner = rossa
    elif colore == 'verde':
        winner = verde
    screen.fill((0, 0, 0))
    screen.blit(winner, (598,445))
    screen.blit(winner_text, (150,180))
    screen.blit(coppa, (200,345))
    pygame.display.update()
    loop=True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop=False
    pygame.quit()

vel = 10
arancio_win, azzurra_win, rossa_win, verde_win = 0,0,0,0
inizzializza()
loop=True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                x_arancio += vel
                if x_arancio > 710:
                    arancio_win += 1
                    vittoria('arancio')
            if event.key == pygame.K_r:
                x_azzurra += vel
                if x_azzurra > 710:
                    azzurra_win+=1
                    vittoria('azzurra')
            if event.key == pygame.K_u:
                x_rossa += vel
                if x_rossa > 710:
                    rossa_win+=1
                    vittoria('rossa')
            if event.key == pygame.K_p:
                x_verde += vel
                if x_verde > 710:
                    verde_win+=1
                    vittoria('verde')
    aggiorna()
    clock.tick(60)
    pygame.display.update()
pygame.quit()