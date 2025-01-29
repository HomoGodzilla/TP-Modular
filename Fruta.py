import random

class Fruta:
    def __init__(self,ALTURA,LARGURA,TAMANHO_BLOCO):
        self.ALTURA = ALTURA
        self.LARGURA = LARGURA
        self.TAMANHO_BLOCO = TAMANHO_BLOCO
        self.x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
        self.y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)

    def reposicionar(self):
        self.x = random.randrange(0, self.LARGURA - self.TAMANHO_BLOCO, self.TAMANHO_BLOCO)
        self.y = random.randrange(0, self.ALTURA - self.TAMANHO_BLOCO, self.TAMANHO_BLOCO)