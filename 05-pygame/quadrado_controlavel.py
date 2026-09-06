import pygame

pygame.init()

# Criar janela
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu primeiro jogo")

# Posição do quadrado
x = 100
y = 100

# Velocidade
velocidade = 5

# Loop principal
rodando = True
clock = pygame.time.Clock()

while rodando:

    # FPS
    clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Teclas pressionadas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        x += velocidade

    if teclas[pygame.K_LEFT]:
        x -= velocidade

    if teclas[pygame.K_UP]:
        y -= velocidade

    if teclas[pygame.K_DOWN]:
        y += velocidade

    # impedir sair pela esquerda
    if x < 0:
        x = 0

    # impedir sair pela direita
    if x > 700:
        x = 700

    # impedir sair por cima
    if y < 0:
        y = 0

    # impedir sair por baixo
    if y > 500:
        y = 500

    # Fundo verde
    janela.fill((0, 245, 20))

    # Desenhar quadrado vermelho
    pygame.draw.rect(janela, (200, 0, 0), (x, y, 100, 100))

    # Atualizar tela
    pygame.display.update()

pygame.quit()
