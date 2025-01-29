import pygame
import Fruta
import Cobra

# Configurações globais
TAMANHO_BLOCO = 20
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

class Game:
    def __init__(self,LARGURA,ALTURA,SCORE):
        self.LARGURA = LARGURA
        self.ALTURA = ALTURA
        self.HIGHSCORE = SCORE
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.clock = pygame.time.Clock()
        self.cabeca = Cobra.Cabeça(LARGURA // 2, ALTURA // 2)
        self.corpo = Cobra.Corpo()
        self.fruta = Fruta.Fruta(ALTURA,LARGURA,TAMANHO_BLOCO)
        self.running = True

    def verificar_colisao(self):
        # Colisão com bordas
        if self.cabeca.x < 0 or self.cabeca.x >= self.LARGURA or self.cabeca.y < 0 or self.cabeca.y >= self.ALTURA:
            self.running = False

        # Colisão com o corpo
        if self.corpo.colidiu_com_cabeca((self.cabeca.x, self.cabeca.y)):
            self.running = False

    def verificar_comida(self):
        if self.cabeca.x == self.fruta.x and self.cabeca.y == self.fruta.y:
            self.fruta.reposicionar()
            self.corpo.crescer()

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

            pygame.display.update()
            self.clock.tick(10)

        pygame.quit()

if __name__ == "__main__":
    with open('settings.txt', 'r') as arquivo:
        tosplit=arquivo.readline()
        LARGURA=tosplit.split(" ")
        tosplit=arquivo.readline()
        ALTURA=tosplit.split(" ")
        tosplit=arquivo.readline()
        SCORE=tosplit.split(" ")
        #FEIO PRA KRL, MAS TA FUNCIONANDO DPS EU ARRUMO
    jogo = Game(int(LARGURA[1]),int(ALTURA[1]),int(SCORE[1]))
    jogo.loop_principal()