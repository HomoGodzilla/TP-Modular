import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)

class Menu:
    def __init__(self, LARGURA, ALTURA):
        self.LARGURA = LARGURA
        self.ALTURA = ALTURA
        self.fonte = pygame.font.Font("./font/VCR.ttf", int(ALTURA * 0.1))
        self.opcoes = ["JOGAR", "DESBLOQUEIOS","OPCOES", "SAIR"]
        self.selecionado = 0

    def desenhar_menu(self, tela):
        tela.fill(PRETO)
        for i, opcao in enumerate(self.opcoes):
            cor = AMARELO if i == self.selecionado else BRANCO
            texto = self.fonte.render(opcao, True, cor)
            pos_x = self.LARGURA // 2 - texto.get_width() // 2
            pos_y = self.ALTURA // 2 - texto.get_height() // 2 + i * int(self.ALTURA * 0.1)
            tela.blit(texto, (pos_x, pos_y))

    def mover_selecao(self, direcao):
        if direcao == "UP":
            self.selecionado = (self.selecionado - 1) % len(self.opcoes)
        elif direcao == "DOWN":
            self.selecionado = (self.selecionado + 1) % len(self.opcoes)

    def selecionar(self):
        return self.opcoes[self.selecionado]