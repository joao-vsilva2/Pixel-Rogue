# 🎮 Pixel Rogue: Labirinto das Sombras

> Um jogo rogue em pixel art com herói, inimigos aleatórios e sistema de som.

Um pequeno jogo desenvolvido com Python e Pygame Zero (`pgzero`) que simula um estilo "Rogue", onde o jogador controla um herói que deve evitar colisões com inimigos aleatórios em um labirinto sombrio.

---

## 🧩 Funcionalidades

- Menu inicial interativo (Iniciar, Ativar/Desativar som, Sair)
- Herói com animação e movimentação suave
- Inimigos com movimento aleatório e limitado a uma área
- Sons:
  - Música de fundo ambiente
  - Som de passos ao mover o herói
  - Som de dano ao colidir com inimigo
- Sistema de reinicialização após "Game Over"
- Detecção de colisão entre herói e inimigos

---

## 📦 Estrutura do Projeto

```
Projeto Prático/
├── jogo.py                  # Código principal do jogo
├── music/                   # Pasta com arquivos de áudio
│   ├── background_music.ogg # Música de fundo
│   ├── hero_walk.ogg        # Som dos passos do herói
│   └── enemy_hit.ogg        # Som de dano ao tocar no inimigo
└── images/                  # Pasta com imagens do jogo
    ├── hero_walk_0.png      # Animações do herói
    ├── hero_walk_1.png
    ├── hero_walk_2.png
    ├── hero_walk_3.png
    ├── enemy_idle_0.png     # Animações do inimigo
    ├── enemy_idle_1.png
    ├── enemy_idle_2.png
    └── enemy_idle_3.png
```

---

## ⚙️ Requisitos

Para rodar o jogo, você precisa ter instalado:

- [Python 3.x](https://www.python.org/)
- Bibliotecas:
  - `pygame-zero` (`pgzero`)
  - `pygame` (instalado automaticamente com `pgzero`)

### Instalação

```bash
pip install pygame-zero
```

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Certifique-se de que as pastas `music/` e `images/` estão corretamente preenchidas com os recursos necessários.

3. Execute o jogo:

```bash
python jogo.py
```

---

## 🕹️ Controles

- **Setas do teclado** ou **WASD** → Movimentar o herói 
- **Clique nos botões** do menu → Iniciar, Ativar/Desativar som ou Sair 
- **Espaço (SPACE)** → Reiniciar o jogo após Game Over 

---

## 📝 Créditos

- Desenvolvimento: *João Silva* 
- Arte:
  - Herói: *Próprio desenvolvedor*
  - Inimigo: *Próprio desenvolvedor* 
- Áudio: *Créditos aos criadores dos sons utilizados*

---

### Game


