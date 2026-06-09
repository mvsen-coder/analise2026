from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

# 1. INICIALIZAÇÃO
app = Ursina()

# Desativa as mensagens de texto padrão do modo de desenvolvedor
application.development_mode = False

# 2. ADICIONANDO O CÉU
# Isso substitui o fundo cinza por um céu azul com nuvens automático da Ursina
ceu = Sky()

# 3. CRIANDO O CHÃO COM FÍSICA
chao = Entity(
    model='cube',
    scale=(100, 1, 100),       # 100 de largura, 1 de altura, 100 de comprimento
    color=color.dark_gray,     # Cor cinza escuro para o chão
    position=(0, -0.5, 0),     # Posicionado um pouco abaixo do nível zero
    collider='box'             # IMPORTANTE: Cria a física para o jogador ficar de pé!
)

# 4. ADICIONANDO PILARES COLORIDOS (Pontos de referência)
# Vamos espalhar 20 pilares pelo mapa para você ter o que olhar e desviar
cores = [color.red, color.green, color.blue, color.yellow, color.orange, color.violet]

for i in range(20):
    # Gera posições aleatórias para os pilares
    x_aleatorio = random.randint(-30, 30)
    z_aleatorio = random.randint(10, 40)   # Coloca a maioria na frente de onde o jogador nasce
    altura_aleatoria = random.randint(3, 8) # Alturas diferentes
    cor_aleatoria = random.choice(cores)    # Cor aleatória
    
    Entity(
        model='cube',
        scale=(2, altura_aleatoria, 2),
        position=(x_aleatorio, altura_aleatoria / 2, z_aleatorio),
        color=cor_aleatoria,
        collider='box' # Os pilares também têm física, você não consegue atravessá-los
    )

# 5. CONTROLE DO JOGADOR (Primeira Pessoa)
# Cria o personagem com câmera livre no mouse e controles WASD
jogador = FirstPersonController()
jogador.y = 2              # Faz o jogador nascer no alto e cair em cima do chão em segurança
jogador.cursor.visible = True # Mostra uma mirinha no centro da tela

# 6. LÓGICA DE ATUALIZAÇÃO (Game Loop)
def update():
    # Se você se perder ou conseguir cair do mapa, aperte a tecla 'R' para resetar a posição
    if held_keys['r']:
        jogador.position = (0, 2, 0)

# Inicia o jogo
app.run()