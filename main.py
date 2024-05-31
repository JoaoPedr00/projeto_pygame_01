from game_init import *
import game_functions

musica_1 = pygame.mixer.music.load("pixel-song-21-72593.mp3")
pygame.mixer.music.play(loops=-1)
musica_2 = pygame.mixer.Sound("food_G1U6tlb.wav")
# Loop Principal:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        
        # Controlando a cobrinha:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if y_controle != velocidade:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == pygame.K_a:
                if x_controle != velocidade:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == pygame.K_s:
                if y_controle != -velocidade:
                    x_controle = 0
                    y_controle = velocidade
            if event.key == pygame.K_d:
                if x_controle != -velocidade:
                    x_controle = velocidade
                    y_controle = 0

    # Primeira instrução do jogo:
    clock.tick(40)
    tela.fill((0, 0, 0))
    matchScore = f'Score: {pontos}'
    txt = fonte.render(matchScore, True, (0, 0, 255))
    end_message = 'Game Over!'
    txt2 = fonte.render(end_message,True,(0,0,255))
    x_cobrinha += x_controle
    y_cobrinha += y_controle
   
    if x_cobrinha >= largura_tela:
        x_cobrinha = 1
    if x_cobrinha <= 0:
        x_cobrinha = largura_tela
    if y_cobrinha >= altura_tela:
        y_cobrinha = 1
    if y_cobrinha <= 0:
        y_cobrinha = altura_tela

    cobrinha = pygame.draw.rect(tela, (0, 255, 0), (x_cobrinha, y_cobrinha, largura_objeto_cobrinha, altura_objeto_cobrinha))    
    comidinha = pygame.draw.rect(tela, (255, 0, 0), (x_comidinha, y_comidinha, largura_objeto_comidinha, altura_objeto_comidinha))

    lista_cabeca_cobrinha = []
    lista_cabeca_cobrinha.append(x_cobrinha)
    lista_cabeca_cobrinha.append(y_cobrinha)

    lista_cobrinha.append(lista_cabeca_cobrinha)
    
    # Fim do jogo:
    if lista_cobrinha.count(lista_cabeca_cobrinha) > 1:
        while 1:
            tela.fill((0,0,0))
            tela.blit(txt2,(largura_tela/2,altura_tela/2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
                if event.type == pygame.KEYDOWN:
                    pygame.key == pygame.K_RETURN: 
                        # Especificações de tamanho e posição da Cobrinha:
                        largura_objeto_cobrinha = 10
                        altura_objeto_cobrinha = 10

                        x_cobrinha = largura_tela/2 - largura_objeto_cobrinha/2
                        y_cobrinha = altura_tela/2 - altura_objeto_cobrinha/2

                        lista_cobrinha = []
                        comprimento = 3 

                        # Especificações de tamanho e posição da Comidinha:
                        largura_objeto_comidinha = 10
                        altura_objeto_comidinha = 10

                        x_comidinha = random.randint(10, 620)
                        y_comidinha = random.randint(10, 460)

                        # Especificações de controle:
                        velocidade = 5
                        x_controle = velocidade
                        y_controle = 0
                        pontos = 0
                        break
            pygame.display.update()


    if len(lista_cobrinha) > comprimento:
        del lista_cobrinha[0]

    game_functions.esticar_cobrinha(tela, lista_cobrinha)

    if cobrinha.colliderect(comidinha):
        x_comidinha = random.randint(10, 620)
        y_comidinha = random.randint(10, 460)
        comprimento += 1
        pontos += 1
        musica_2.play()

        if pontos % 10 == 0:
            velocidade += 1

    

    


    tela.blit(txt, (520, 30))
    pygame.display.update()