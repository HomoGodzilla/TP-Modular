import pygame
import time
import Cobra
import Fruta

PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (50, 50, 50)
AMARELO = (255, 255, 0)

TAMANHO_BLOCO = 20

class Game:
    def __init__(self, LARGURA, ALTURA, SCORE):
        self.LARGURA = LARGURA
        self.ALTURA = ALTURA
        self.HIGHSCORE = SCORE
        self.JOGO_LARGURA = int(LARGURA * 0.8)
        self.INFO_LARGURA = LARGURA - self.JOGO_LARGURA
        self.JOGO_ALTURA = ALTURA
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.clock = pygame.time.Clock()
        self.cabeca = Cobra.Cabeça(self.JOGO_LARGURA // 2, self.JOGO_ALTURA // 2)
        self.corpo = Cobra.Corpo()
        self.fruta = Fruta.Fruta(self.JOGO_ALTURA, self.JOGO_LARGURA, TAMANHO_BLOCO)
        self.running = True
        self.start_time = time.time()
        self.fonte = pygame.font.SysFont(None, int(ALTURA * 0.05))

    def verificar_colisao(self):
        if self.cabeca.x < 0 or self.cabeca.x >= self.JOGO_LARGURA or self.cabeca.y < 0 or self.cabeca.y >= self.JOGO_ALTURA:
            self.running = False
        if self.corpo.colidiu_com_cabeca((self.cabeca.x, self.cabeca.y)):
            self.running = False

    def verificar_comida(self):
        if self.cabeca.x == self.fruta.x and self.cabeca.y == self.fruta.y:
            self.fruta.reposicionar()
            self.corpo.crescer()

    def mostrar_informacoes(self):
        pygame.draw.rect(self.tela, CINZA, [self.JOGO_LARGURA, 0, self.INFO_LARGURA, self.ALTURA])
        score_text = self.fonte.render(f"Score: {len(self.corpo.partes)}", True, BRANCO)
        tempo_text = self.fonte.render(f"Tempo: {int(time.time() - self.start_time)}s", True, BRANCO)
        self.tela.blit(score_text, (self.JOGO_LARGURA + 10, 20))
        self.tela.blit(tempo_text, (self.JOGO_LARGURA + 10, 60))

    def loop_principal(self):
        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.cabeca.mudar_direcao(0, -TAMANHO_BLOCO)
                    elif evento.key == pygame.K_DOWN:
                        self.cabeca.mudar_direcao(0, TAMANHO_BLOCO)
                    elif evento.key == pygame.K_LEFT:
                        self.cabeca.mudar_direcao(-TAMANHO_BLOCO, 0)
                    elif evento.key == pygame.K_RIGHT:
                        self.cabeca.mudar_direcao(TAMANHO_BLOCO, 0)

            self.cabeca.mover()
            self.corpo.atualizar((self.cabeca.x, self.cabeca.y))
            self.verificar_colisao()
            self.verificar_comida()

            self.tela.fill(PRETO)
            pygame.draw.rect(self.tela, VERMELHO, [self.fruta.x, self.fruta.y, TAMANHO_BLOCO, TAMANHO_BLOCO])
            for parte in self.corpo.partes:
                pygame.draw.rect(self.tela, VERDE, [parte[0], parte[1], TAMANHO_BLOCO, TAMANHO_BLOCO])
            pygame.draw.rect(self.tela, VERDE, [self.cabeca.x, self.cabeca.y, TAMANHO_BLOCO, TAMANHO_BLOCO])

            self.mostrar_informacoes()
            pygame.display.update()
            self.clock.tick(10)

