import pygame
# pylint: disable=no-member

## tamanho do ecrâ
pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)

## cores base
black = (0, 0, 0)
white = (255, 255, 255)
Normal_Yellow = (150, 150, 0)
Bright_Yellow = (200, 200, 0)
Normal_Blue = (40, 30, 250)

## fontes base
textopequeno = pygame.font.Font("OpenSans-Regular.ttf", 20)

## função para tratar das caixas de texto
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

## função para tratar dos botões do menu
def button(mensagem, x, y, comprimento, altura, cor_ativa, cor_inativa, evento):

    ## obter posição e clicks do rato
    posição_do_rato = pygame.mouse.get_pos()
    click_do_rato = pygame.mouse.get_pressed()
    
    ## confirmar se o rato se encontra dentro dos limites dos botões
    if (x+comprimento > posição_do_rato[0] > x and y + altura > posição_do_rato[1] > y):
        ## Desenhar retangulos ativos
        pygame.draw.rect(screen, cor_ativa, (x, y, comprimento, altura))
        superficie_do_texto, retangulo_do_texto = text_objects(mensagem, textopequeno, black)
        retangulo_do_texto.center = ( (x + (comprimento/2)), (y + (altura/2)) )
        screen.blit(superficie_do_texto, retangulo_do_texto)

        ## decidir o que fazer dependendo de que botão clicar
        if (evento == "quitgame" and click_do_rato[0] == 1):
            pygame.quit()
            quit()

    else:
        ## Desenhar retangulos inativos
        pygame.draw.rect(screen, cor_inativa, (x, y, comprimento, altura), 1)
        superficie_do_texto, retangulo_do_texto = text_objects(mensagem, textopequeno, white)
        retangulo_do_texto.center = ( (x + (comprimento/2)), (y + (altura/2)) )
        screen.blit(superficie_do_texto, retangulo_do_texto)

## função para dar print ao menu
def menu():

    while(True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            
            screen.fill(black)
            button("3 x 4", 590, 300, 100, 40, Bright_Yellow, Normal_Yellow, "game3x4")
            button("4 x 4", 590, 350, 100, 40, Bright_Yellow, Normal_Yellow, "game4x4")
            button("5 x 4", 590, 400, 100, 40, Bright_Yellow, Normal_Yellow, "game5x4")
            button("6 x 4", 590, 450, 100, 40, Bright_Yellow, Normal_Yellow, "game6x4")
            button("6 x 5", 590, 500, 100, 40, Bright_Yellow, Normal_Yellow, "game6x5")
            button("6 x 6", 590, 550, 100, 40, Bright_Yellow, Normal_Yellow, "game6x6")
            button("Exit", 80, 620, 100, 40, Bright_Yellow, Normal_Yellow, "quitgame")
            button
            pygame.display.flip()


menu()