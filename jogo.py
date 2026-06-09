import pygame
import random
import sys

# 1. INICIALIZAÇÃO
pygame.init()

# Configurações da tela
LARGURA = 600
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desvio Espacial")

# Cores (Padrão RGB)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Controlar a velocidade de quadros (FPS)
relogio = pygame.time.Clock()
FPS = 60

# Fonte para o texto
fonte = pygame.font.SysFont("monospace", 30)

# 2. VARIÁVEIS DO JOGO
# Jogador
jogador_tamanho = 40
jogador_x = LARGURA // 2 - jogador_tamanho // 2
jogador_y = ALTURA - 70
jogador_velocidade = 8

# Inimigos (Asteroides)
inimigo_tamanho = 40
inimigo_posicoes = [] # Lista que vai guardar os inimigos activos
inimigo_velocidade = 5
temporizador_inimigo = 0

# Pontuação
pontos = 0
game_over = False

def criar_inimigo():
    """Cria um inimigo em uma posição X aleatória no topo da tela"""
    x_aleatorio = random.randint(0, LARGURA - inimigo_tamanho)
    y_inicial = -inimigo_tamanho
    return [x_aleatorio, y_inicial]

# 3. LOOP PRINCIPAL DO JOGO
while True:
    
    # SE O JOGO ACABOU (TELA DE GAME OVER)
    while game_over:
        tela.fill(PRETO)
        texto_game_over = fonte.render("GAME OVER", True, VERMELHO)
        texto_pontos = fonte.render(f"Pontos Finais: {pontos}", True, BRANCO)
        texto_reiniciar = fonte.render("Pressione ESPAÇO para reiniciar", True, BRANCO)
        
        # Desenha os textos centralizados
        tela.blit(texto_game_over, (LARGURA // 2 - 80, ALTURA // 2 - 60))
        tela.blit(texto_pontos, (LARGURA // 2 - 120, ALTURA // 2))
        tela.blit(texto_reiniciar, (LARGURA // 2 - 250, ALTURA // 2 + 60))
        
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    # Reinicia todas as variáveis para recomeçar
                    jogador_x = LARGURA // 2 - jogador_tamanho // 2
                    inimigo_posicoes = []
                    inimigo_velocidade = 5
                    pontos = 0
                    game_over = False

    # 4. CAPTURA DE EVENTOS (Enquanto o jogo está rodando)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles do jogador (Pressionar e segurar as setas)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= jogador_velocidade
    if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - jogador_tamanho:
        jogador_x += jogador_velocidade

    # 5. LÓGICA DO JOGO
    # Criar novos inimigos ao longo do tempo
    temporizador_inimigo += 1
    if temporizador_inimigo > 30: # Cria um inimigo a cada ~0.5 segundos
        inimigo_posicoes.append(criar_inimigo())
        temporizador_inimigo = 0

    # Atualizar posição dos inimigos e checar colisões
    for inimigo in inimigo_posicoes[:]:
        inimigo[1] += inimigo_velocidade # Move para baixo
        
        # Se o inimigo saiu da tela por baixo
        if inimigo[1] > ALTURA:
            inimigo_posicoes.remove(inimigo)
            pontos += 1
            # Aumenta a velocidade a cada 5 pontos (Dificuldade progressiva)
            if pontos % 5 == 0:
                inimigo_velocidade += 1

        # Sistema de Colisão (Se o quadrado do jogador cruzar com o do inimigo)
        if (inimigo[1] + inimigo_tamanho > jogador_y and 
            inimigo[1] < jogador_y + jogador_tamanho): # Alinhamento Y
            if (inimigo[0] + inimigo_tamanho > jogador_x and 
                inimigo[0] < jogador_x + jogador_tamanho): # Alinhamento X
                game_over = True

    # 6. DESENHOS NA TELA
    tela.fill(PRETO) # Limpa a tela com fundo preto

    # Desenha o jogador (Quadrado Verde)
    pygame.draw.rect(tela, VERDE, (jogador_x, jogador_y, jogador_tamanho, jogador_tamanho))

    # Desenha os inimigos (Quadrados Vermelhos)
    for inimigo in inimigo_posicoes:
        pygame.draw.rect(tela, VERMELHO, (inimigo[0], inimigo[1], inimigo_tamanho, inimigo_tamanho))

    # Desenha o placar de pontos
    texto_placar = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_placar, (10, 10))

    # Atualiza a tela e controla o FPS
    pygame.display.flip()
    relogio.tick(FPS)