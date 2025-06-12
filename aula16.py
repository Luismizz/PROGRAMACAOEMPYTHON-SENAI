import pygame

pygame.init()

tamanho = 500, 500
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Jogo Pin-Pong")

CINZA = (54, 54, 54)
PRETO = (0, 0, 0)


raquete1_x, raquete1_y = 50, 225
raquete2_x, raquete2_y = 450, 225

ball_x, ball_y = 250, 250
velocidade_bola_x = 2.5
velocidade_bola_y = 2.5
velocidade_raquete = 5


raquete_altura, largura_raquete = 100, 20
bola_largura, bola_altura = 20, 20


placar1 = 0
placar2 = 0

font = pygame.font.SysFont(None, 55)

def desenhar():
    tela.fill(CINZA)

    pygame.draw.rect(tela, PRETO, (raquete1_x, raquete1_y, largura_raquete, raquete_altura))
    pygame.draw.rect(tela, PRETO, (raquete2_x, raquete2_y, largura_raquete, raquete_altura))
    pygame.draw.ellipse(tela, PRETO, (ball_x, ball_y, bola_largura, bola_altura))

    placar_texto = font.render(f'{placar1} | {placar2}', True, PRETO)
    tela.blit(placar_texto, (200, 20))

LOOP = True
clock = pygame.time.Clock()

while LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            LOOP = False  

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y + raquete_altura < 500:
        raquete1_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y + raquete_altura < 500:
        raquete2_y += velocidade_raquete

    ball_x += velocidade_bola_x
    ball_y += velocidade_bola_y  
    
    # Colisão com bordas horizontais
    if ball_y <= 0 or ball_y + bola_altura >= 500:
        velocidade_bola_y *= -1

    # Colisão com raquetes
    if (raquete1_x < ball_x < raquete1_x + largura_raquete) and (raquete1_y < ball_y < raquete1_y + raquete_altura):
        velocidade_bola_x *= -1

    if (raquete2_x < ball_x + bola_largura < raquete2_x + largura_raquete) and (raquete2_y < ball_y < raquete2_y + raquete_altura):
        velocidade_bola_x *= -1

    # Pontuação
    if ball_x <= 0:
        placar2 += 1
        ball_x, ball_y = 250, 250
        velocidade_bola_x *= -1
    elif ball_x + bola_largura >= 500:
        placar1 += 1
        ball_x, ball_y = 250, 250
        velocidade_bola_x *= -1

    desenhar()
    pygame.display.update()
    clock.tick(60)  # Controle de FPS

pygame.quit()
