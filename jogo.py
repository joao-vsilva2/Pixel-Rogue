import pgzrun
import random
from pygame import Rect
from pgzero.actor import Actor

# Função para obter tamanho das imagens
def tamanho_imagem(image_name):
    try:
        temp = Actor(image_name)
        return (temp.width, temp.height)
    except Exception as e:
        print(f"Imagem '{image_name}' não encontrada!")
        return (0, 0)

# Configurações do jogo
TITLE = "Pixel Rogue: Labirinto das Sombras"
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 40
HERO_SPEED = 100
ENEMY_SPEED = 50
ANIM_FRAME_RATE = 0.1

# Estados do jogo
inicio_jogo = "menu"  # menu / jogando / game_over
som_ativo = True

# Sons do jogo
som_passos = None
som_colisao = None

if som_ativo:
    try:
        som_passos = sounds.hero_walk
    except Exception as e:
        print("Erro ao carregar som de passos:", e)

    try:
        som_colisao = sounds.enemy_hit
    except Exception as e:
        print("Erro ao carregar som de colisão:", e)

# Classes
class SpriteAnimado:
    def __init__(self, lista_imagem, pos):
        self.images = [f"{img}" for img in lista_imagem]
        self.image_index = 0
        self.x, self.y = pos
        self.last_update = 0
        self.width, self.height = tamanho_imagem(self.images[0])

    @property
    def imagem(self):
        return self.images[self.image_index]

    @property
    def rect(self):
        return Rect((self.x, self.y), (self.width, self.height))

    def atualizar_animacao(self, dt):
        self.last_update += dt
        if self.last_update > ANIM_FRAME_RATE:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.last_update = 0

    def draw(self):
        screen.blit(self.imagem, (self.x, self.y))


class Hero(SpriteAnimado):
    def __init__(self, pos):
        super().__init__([f'hero_walk_{i}' for i in range(4)], pos)

    def move(self, dx, dy, dt):
        self.x += dx * HERO_SPEED * dt
        self.y += dy * HERO_SPEED * dt
        self.atualizar_animacao(dt)
        if som_ativo and som_passos:
            som_passos.play()


class Enemy(SpriteAnimado):
    def __init__(self, pos):
        super().__init__([f'enemy_idle_{i}' for i in range(4)], pos)
        self.move_timer = 0
        self.dir = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.start_x, self.start_y = pos

    def update(self, dt):
        self.move_timer += dt
        if self.move_timer > random.uniform(0.5, 1.5):
            self.dir = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            self.move_timer = 0

        new_x = self.x + self.dir[0] * ENEMY_SPEED * dt
        new_y = self.y + self.dir[1] * ENEMY_SPEED * dt

        if abs(new_x - self.start_x) < 100 and abs(new_y - self.start_y) < 100:
            self.x = new_x
            self.y = new_y

        self.atualizar_animacao(dt)


# Objetos do jogo
try:
    heroi = Hero((WIDTH // 2, HEIGHT // 2))
    inimigos = [Enemy((random.randint(0, WIDTH), random.randint(0, HEIGHT))) for _ in range(7)]
except Exception as e:
    print("Erro ao criar objetos do jogo:", e)
    exit()

# Botões do menu
botao_inicio = Rect(300, 200, 200, 50)
botao_som = Rect(300, 300, 200, 50)
botao_sair = Rect(300, 400, 200, 50)

# Evento de clique do mouse
def on_mouse_down(pos):
    global inicio_jogo, som_ativo
    if inicio_jogo == "menu":
        if botao_inicio.collidepoint(pos):
            inicio_jogo = "jogando"
        elif botao_som.collidepoint(pos):
            som_ativo = not som_ativo
            if som_ativo:
                music.unpause()
            else:
                music.pause()
        elif botao_sair.collidepoint(pos):
            exit()

# Atualização lógica
def update(dt):
    global inicio_jogo

    if inicio_jogo == "menu":
        if som_ativo and not music.is_playing("som de fundo"):
            music.play("som de fundo")

    elif inicio_jogo == "jogando":
        dx = keyboard.RIGHT - keyboard.LEFT
        dy = keyboard.DOWN - keyboard.UP
        heroi.move(dx, dy, dt)

        for inimigo in inimigos:
            inimigo.update(dt)

        # Verifica colisão
        for inimigo in inimigos:
            if heroi.rect.colliderect(inimigo.rect):
                if som_ativo and som_colisao:
                    som_colisao.play()
                inicio_jogo = "game_over"

    elif inicio_jogo == "game_over":
        if keyboard.SPACE:
            redefinir_jogo()

# Função para reiniciar o jogo
def redefinir_jogo():
    global heroi, inimigos, inicio_jogo
    heroi = Hero((WIDTH // 2, HEIGHT // 2))
    inimigos = [Enemy((random.randint(0, WIDTH), random.randint(0, HEIGHT))) for _ in range(7)]
    inicio_jogo = "jogando"

# Renderização
def draw():
    screen.clear()
    if inicio_jogo == "menu":
        screen.draw.filled_rect(botao_inicio, (70, 130, 180))
        screen.draw.text("Iniciar Jogo", center=botao_inicio.center, fontsize=30, color="white")

        screen.draw.filled_rect(botao_som, (70, 130, 180))
        screen.draw.text(f"Som: {'On' if som_ativo else 'Off'}", center=botao_som.center, fontsize=30, color="white")

        screen.draw.filled_rect(botao_sair, (70, 130, 180))
        screen.draw.text("Sair", center=botao_sair.center, fontsize=30, color="white")

    elif inicio_jogo == "jogando":
        heroi.draw()
        for enemy in inimigos:
            enemy.draw()

    elif inicio_jogo == "game_over":
        screen.draw.text("Game Over!", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        screen.draw.text("Pressione 'SPACE' para recomeçar", center=(WIDTH//2, HEIGHT//2 + 50), fontsize=30, color="white")

# Roda o jogo
pgzrun.go()