class Cabeça:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def mover(self):
        self.x += self.dx
        self.y += self.dy

    def mudar_direcao(self, dx, dy):
        if (self.dx == 0 or dx == 0) and (self.dy == 0 or dy == 0):  # Evitar reversão
            self.dx = dx
            self.dy = dy

class Corpo:
    def __init__(self):
        self.partes = []

    def atualizar(self, cabeca_pos):
        self.partes.append(cabeca_pos)
        if len(self.partes) > 1:
            self.partes.pop(0)

    def crescer(self):
        self.partes.append(self.partes[-1])

    def colidiu_com_cabeca(self, cabeca_pos):
        return cabeca_pos in self.partes[:-1]