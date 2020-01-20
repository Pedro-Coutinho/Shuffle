import pygame
import random
# pylint: disable=no-member

## tamanho do ecrâ
pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)

## Cores base
black = (0, 0, 0)
white = (255, 255, 255)
Normal_Yellow = (150, 150, 0)
Bright_Yellow = (200, 200, 0)

## Fontes base
textopequeno = pygame.font.Font("OpenSans-Regular.ttf", 20)
textogrande = pygame.font.Font("viking_elder_runes_bold.ttf", 140)
clock = pygame.time.Clock()
clock.tick(30)

## Dar load à musica e defenir o volume
pygame.mixer_music.load("Production Music - Nordic Chill.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer_music.play(-1)

# Dar load aos sons e defenir o volume
buttonSound = pygame.mixer.Sound("ButtonClick.wav")
buttonSound.set_volume(0.1)


## Função para tratar do texto
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

## Função para tratar dos botões
def button(mensagem, x, y, comprimento, altura, cor_ativa, cor_inativa, evento):

    ## Obter posição e clicks do rato
    posição_do_rato = pygame.mouse.get_pos()
    click_do_rato = pygame.mouse.get_pressed()
    
    ## Confirmar se o rato se encontra dentro dos limites dos botões
    if (x+comprimento > posição_do_rato[0] > x and y + altura > posição_do_rato[1] > y):
        ## Dar draw dos retangulos ativos
        pygame.draw.rect(screen, cor_ativa, (x, y, comprimento, altura))
        superficie_do_texto, retangulo_do_texto = text_objects(mensagem, textopequeno, black)
        retangulo_do_texto.center = ( (x + (comprimento/2)), (y + (altura/2)) )
        screen.blit(superficie_do_texto, retangulo_do_texto)

        ## Decidir o que fazer dependendo de que botão clicar
        if (evento == "quitgame" and click_do_rato[0] == 1):
            buttonSound.play()
            pygame.time.wait(300)
            pygame.quit()
            quit()

        elif (evento == "game3x4" and click_do_rato[0] == 1):
            buttonSound.play()
            levels(12)
        elif (evento == "game4x4" and click_do_rato[0] == 1):
            buttonSound.play()
            levels(16)
        elif (evento == "game4x5" and click_do_rato[0] == 1):
            buttonSound.play()
            levels(20)
        elif (evento == "game6x4" and click_do_rato[0] == 1):
            buttonSound.play()
            levels(24)
        elif (evento == "game6x5" and click_do_rato[0] == 1):
            buttonSound.play()
            levels(30)
        elif (evento == "game6x6" and click_do_rato[0] == 1):
            buttonSound.play()
            levels(36)

        elif (evento == "menu" and click_do_rato[0] == 1):
            buttonSound.play()
            menu()    
    else:
        ## Desenhar retangulos inativos
        pygame.draw.rect(screen, cor_inativa, (x, y, comprimento, altura), 1)
        superficie_do_texto, retangulo_do_texto = text_objects(mensagem, textopequeno, white)
        retangulo_do_texto.center = ( (x + (comprimento/2)), (y + (altura/2)) )
        screen.blit(superficie_do_texto, retangulo_do_texto)

def levels (grid):
    
    ## Defenir as Cartas
    cartas = ["Rune 1.png", "Rune 1.png", "Rune 2.png", "Rune 2.png", "Rune 3.png", "Rune 3.png", "Rune 4.png", "Rune 4.png", "Rune 5.png", "Rune 5.png", "Rune 6.png", "Rune 6.png", "Rune 7.png", "Rune 7.png", "Rune 8.png", "Rune 8.png", "Rune 9.png", "Rune 9.png",
    "Rune 10.png", "Rune 10.png", "Rune 11.png", "Rune 11.png", "Rune 12.png", "Rune 12.png", "Rune 13.png", "Rune 13.png", "Rune 14.png", "Rune 14.png", "Rune 15.png", "Rune 15.png", "Rune 16.png", "Rune 16.png", "Rune 17.png", "Rune 17.png",
    "Rune 18.png", "Rune 18.png"]
    cartasbool = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False,False, False]
    cartaseleminadasbool = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    cartastemp = cartas[:grid]
    random.shuffle(cartastemp)
    
    ## Variaveis para a pausa apos viras 2 cartas
    nCartasViradas = 0
    timeToWait = 0

    #3 Variaveis dos pontos
    pontos = 0
    vezeserrado = 0
    cartavirada1 = "carta"
    cartavirada2 = "carta0"
    nCarta1 = 0
    nCarta2 = 0
    cartaseliminadas = 0

    ## Começar com uma ligeira pausa
    pygame.time.wait(200)
    
    ## Variavél para mudar a cor de fundo
    blue = 0
    

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

        ## Obter a posição do rato e se foi clicado
        posição_do_rato = pygame.mouse.get_pos()
        click_do_rato = pygame.mouse.get_pressed()

        ## Dar draw do fundo
        screen.fill((0,0,blue))
        if blue > 30:
            addcolor = -0.05
        elif blue < 1:
            addcolor = 0.05
        blue = blue + addcolor

        ## Prender os pontos a um minimo de 0 para não se tornarem negativos
        if pontos < 0:
            pontos = 0

        ## Dar draw dos pontos
        superficie_do_texto, retangulo_do_texto = text_objects("Score: ", textopequeno, white)
        retangulo_do_texto.center = ( (50 + (90/2)), (0 + (135/2)) )
        screen.blit(superficie_do_texto, retangulo_do_texto)
        superficie_do_texto, retangulo_do_texto = text_objects(str(pontos), textopequeno, white)
        retangulo_do_texto.center = ( (110 + (90/2)), (0 + (135/2)) )
        screen.blit(superficie_do_texto, retangulo_do_texto)

        ## Verificar se ainda existem cartas em jogo
        if cartaseliminadas == grid + 1:
            superficie_do_texto, retangulo_do_texto = text_objects("CONGRATS", textogrande, white)
            retangulo_do_texto.center = ( 640 , 360)
            screen.blit(superficie_do_texto, retangulo_do_texto)
            
        if cartaseliminadas == grid:
            cartaseliminadas += 1

        ## Dar draw do botão de saida
        button("Exit", 80, 620, 100, 40, Bright_Yellow, Normal_Yellow, "menu")
        
        ## Defenir a pausa
        if nCartasViradas == 2:
            timeToWait = 1000
                    
        ## Verificar o tamanho do jogo
        ## Defenir as variáveis para desenhar as cartas
        ## Jogo 4 x 3
        if grid == 12:
            x = 430
            xtemp = 430
            y = 100
            comprimento = 90
            altura = 135
            espaço = 40
            i = 0
        ## Verificar o tamanho do jogo        
        ## 4 x 4
        elif grid == 16:
            x = 395
            xtemp = 395
            y = 30
            comprimento = 90
            altura = 135
            espaço = 40
            i = 0   
        ## 4 x 5
        elif grid == 20:
            x = 350
            xtemp = 350
            y = 30
            comprimento = 90
            altura = 135
            espaço = 40
            i = 0
         ## 6 x 4
        elif grid == 24:
            x = 512
            xtemp = 512
            y = 20
            comprimento = 55
            espaço = 30
            altura = 95
            i = 0
        ## 6 x 5
        elif grid == 30:
            x = 475
            xtemp = 475
            y = 30
            comprimento = 55
            altura = 95
            i = 0
        ## 6 x 6
        elif grid == 36:
            x = 438
            xtemp = 438
            y = 30
            comprimento = 55
            altura = 95
            espaço = 20
            i = 0
            ## Loop para desenhar as cartas
        while i < grid:           

            ## Obeter a imagem para cada carta especifica
            image = pygame.image.load(cartastemp[i])

            ## Verificar se a carta está virada e se ainda está em jogo
            if cartasbool[i] and cartaseleminadasbool[i]:

                pygame.draw.rect(screen, Normal_Yellow, (x, y, comprimento, altura), 1)
                image = pygame.transform.scale(image,(comprimento - 20 , altura - 20 ))
                screen.blit(image, (x + 10 , y + 10))  

            ## Verificar se a carta ainda está em jogo
            elif cartaseleminadasbool[i]:

                ## Confirmar se o rato se encontra dentro dos limites dos botões e desenhar a carta ativa
                if (x + comprimento > posição_do_rato[0] > x and y + altura > posição_do_rato[1] > y):
                    ## Desenhar retangulos ativos
                    pygame.draw.rect(screen, Bright_Yellow, (x, y, comprimento, altura))

                    ## Confirmar que foi dado um clique na carta
                    if click_do_rato[0]:
                        cartasbool[i] = True
                        buttonSound.play()
                        
                        if nCartasViradas == 0:
                            cartavirada1 = cartastemp[i]
                            nCarta1 = i
                        else: 
                            cartavirada2 = cartastemp[i]
                            nCarta2 = i

                        nCartasViradas += 1

                ## Desenhar carta inativa
                else:
                    pygame.draw.rect(screen, Normal_Yellow, (x, y, comprimento, altura), 1)

            if grid == 12:
                if i == 3 or i == 7:
                    y += altura + espaço
                    x = xtemp
                else:
                    x += comprimento + espaço 

            elif grid == 16:
                if i == 3 or i == 7 or i == 11:
                    y += altura + espaço
                    x = xtemp
                else:
                    x += comprimento + espaço

            ## 4 x 5
            elif grid == 20:
                if i == 4 or i == 9 or i == 14:
                    y += altura + espaço
                    x = xtemp
                else:
                    x += comprimento + espaço

                
            ## 6 x 4
            elif grid == 24:
                if i == 3 or i == 7 or i == 11 or i == 15 or i == 19:
                    y += altura + espaço
                    x = xtemp
                else:
                    x += comprimento + espaço

                
            ## 6 x 5
            elif grid == 30:
                if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
                    y += altura + espaço
                    x = xtemp
                else:
                    x += comprimento + espaço

                
            ## 6 x 6
            elif grid == 36:
                if i == 5 or i == 11 or i == 17 or i == 23 or i == 29:
                    y += altura + espaço
                    x = xtemp
                else:
                    x += comprimento + espaço

            i += 1
    
        ##Escrever a pontuação
        
        pygame.display.flip()

        if (timeToWait > 0 ):

            if cartavirada1 == cartavirada2:
                cartaseleminadasbool[nCarta1] = False
                cartaseleminadasbool[nCarta2] = False
                cartaseliminadas += 2
                pontos += 100
                vezeserrado = 0
            else:
                vezeserrado += 1
                if vezeserrado > 1:
                    pontos = pontos - ((vezeserrado-1) * 20)
            nCartasViradas = 0
            cartasbool = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False,False, False]
            pygame.time.wait(timeToWait)
            timeToWait = 0

           

            cartavirada1 = "Carta"
            cartavirada2 = "Carta0"

## Função para dar Draw ao menu
def menu(): 
    blue = 0
    pygame.time.wait(200)
    while(True):
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

        
        screen.fill((0, 0, blue))
        ## Draw do titulo
        superficie_do_texto, retangulo_do_texto = text_objects("SHUFFLE", textogrande, white)
        retangulo_do_texto.center = (640, 150)
        screen.blit(superficie_do_texto, retangulo_do_texto)
        ## Draw dos botões
        button("4 x 3", 590, 300, 100, 40, Bright_Yellow, Normal_Yellow, "game3x4")
        button("4 x 4", 590, 350, 100, 40, Bright_Yellow, Normal_Yellow, "game4x4")
        button("5 x 4", 590, 400, 100, 40, Bright_Yellow, Normal_Yellow, "game4x5")
        button("6 x 4", 590, 450, 100, 40, Bright_Yellow, Normal_Yellow, "game6x4")
        button("6 x 5", 590, 500, 100, 40, Bright_Yellow, Normal_Yellow, "game6x5")
        button("6 x 6", 590, 550, 100, 40, Bright_Yellow, Normal_Yellow, "game6x6")
        button("Exit", 590, 600, 100, 40, Bright_Yellow, Normal_Yellow, "quitgame")
        pygame.display.flip()

        ## Mudar cor de fundo
        if blue > 30:
            addcolor = -0.05
        elif blue < 1:
            addcolor = 0.05
        blue = blue + addcolor

menu()