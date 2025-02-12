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
    def __init__(self, LARGURA, ALTURA, SCORE,skin):
        self.LARGURA = LARGURA
        self.ALTURA = ALTURA
        self.HIGHSCORE = SCORE
        self.JOGO_LARGURA = int(LARGURA * 0.8)
        self.INFO_LARGURA = LARGURA - self.JOGO_LARGURA
        self.JOGO_ALTURA = ALTURA
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        self.clock = pygame.time.Clock()
        self.cabeca = Cobra.Cabeça(self.JOGO_LARGURA // 2, self.JOGO_ALTURA // 2)
        self.corpo = Cobra.Corpo()
        self.fruta = Fruta.Fruta(self.JOGO_ALTURA, self.JOGO_LARGURA, TAMANHO_BLOCO)
        self.running = True
        self.start_time = time.time()
        self.fonte = pygame.font.Font("./font/VCR.ttf", int(ALTURA * 0.05))
        self.textura_corpo = skin["corpo"]
        self.textura_cabeca = skin["cabeca"] 
        self.textura_fruta = skin["fruta"]


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
        #score_text = self.fonte.render(f"Score: {len(self.corpo.partes)}", True, BRANCO)
        #highscore_text = self.fonte.render(f"Highscore: {self.HIGHSCORE}", True, BRANCO)
        #tempo_text = self.fonte.render(f"Tempo: {int(time.time() - self.start_time)}s", True, BRANCO)
        score_text = self.fonte.render("Score", True, BRANCO)
        score_value = self.fonte.render(str(len(self.corpo.partes)), True, BRANCO)
        
        highscore_text = self.fonte.render("Highscore", True, BRANCO)
        highscore_value = self.fonte.render(str(self.HIGHSCORE), True, BRANCO)
        
        tempo_text = self.fonte.render("Tempo", True, BRANCO)
        tempo_value = self.fonte.render(f"{int(time.time() - self.start_time)}s", True, BRANCO)
        #self.tela.blit(score_text, (self.JOGO_LARGURA + 10, 20))
        #self.tela.blit(highscore_text, (self.JOGO_LARGURA + 10, 60))
        #self.tela.blit(tempo_text, (self.JOGO_LARGURA + 10, 100))

        self.tela.blit(score_text, (self.JOGO_LARGURA + 10, 10))
        self.tela.blit(score_value, (self.JOGO_LARGURA + 10, 35))
        
        self.tela.blit(highscore_text, (self.JOGO_LARGURA + 10, 70))
        self.tela.blit(highscore_value, (self.JOGO_LARGURA + 10, 95))
        
        self.tela.blit(tempo_text, (self.JOGO_LARGURA + 10, 130))
        self.tela.blit(tempo_value, (self.JOGO_LARGURA + 10, 155))

    def desenhar_objetos(self,pos):
        self.tela.blit(self.textura_fruta,[self.fruta.x, self.fruta.y])
        for parte in self.corpo.partes:
            self.tela.blit(self.textura_corpo, parte)
        textura_cabeca_rotated = pygame.transform.rotate(self.textura_cabeca, pos*90)
        self.tela.blit(textura_cabeca_rotated,[self.cabeca.x, self.cabeca.y])

    def loop_principal(self):
        pos=0
        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.cabeca.mudar_direcao(0, -TAMANHO_BLOCO)
                        pos=0
                    elif evento.key == pygame.K_DOWN:
                        self.cabeca.mudar_direcao(0, TAMANHO_BLOCO)
                        pos=2
                    elif evento.key == pygame.K_LEFT:
                        self.cabeca.mudar_direcao(-TAMANHO_BLOCO, 0)
                        pos=1
                    elif evento.key == pygame.K_RIGHT:
                        self.cabeca.mudar_direcao(TAMANHO_BLOCO, 0)
                        pos=3

            self.cabeca.mover()
            self.corpo.atualizar((self.cabeca.x, self.cabeca.y))
            self.verificar_colisao()
            self.verificar_comida()

            self.tela.fill(PRETO)
            self.desenhar_objetos(pos)
        

            self.mostrar_informacoes()
            pygame.display.update()
            self.clock.tick(10)
        self.HIGHSCORE = len(self.corpo.partes)
        return self.HIGHSCORE

