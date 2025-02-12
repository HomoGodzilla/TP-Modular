import pygame

BRANCO = (255, 255, 255)
CINZA = (50, 50, 50)
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)

SKINS = [
    {
        "nome": "Skin Padrão",
        "arquivos": {
            "cabeca": "skin_padrao_cabeca.png",
            "corpo": "skin_padrao_corpo.png",
            "fruta": "skin_padrao_fruta.png"
        },
        "highscore": 0
    },
    {
        "nome": "Skin Vermelha",
        "arquivos": {
            "cabeca": "skin_vermelha_cabeca.png",
            "corpo": "skin_vermelha_corpo.png",
            "fruta": "skin_vermelha_fruta.png"
        },
        "highscore": 50
    },
    {
        "nome": "Skin Dourada",
        "arquivos": {
            "cabeca": "skin_dourada_cabeca.png",
            "corpo": "skin_dourada_corpo.png",
            "fruta": "skin_dourada_fruta.png"
        },
        "highscore": 100
    },
        {
        "nome": "Skin Bowser",
        "arquivos": {
            "cabeca": "skin_bowser_cabeca.png",
            "corpo": "skin_goomba_corpo.png",
            "fruta": "skin_estrela_fruta.png"
        },
        "highscore": 150
    },
    {
        "nome": "Skin Vermelha",
        "arquivos": {
            "cabeca": "skin_vermelha_cabeca.png",
            "corpo": "skin_vermelha_corpo.png",
            "fruta": "skin_vermelha_fruta.png"
        },
        "highscore": 50
    },
    {
        "nome": "Skin Dourada",
        "arquivos": {
            "cabeca": "skin_dourada_cabeca.png",
            "corpo": "skin_dourada_corpo.png",
            "fruta": "skin_dourada_fruta.png"
        },
        "highscore": 100
    },
]

def carregar_skins():
    for skin in SKINS:
        skin["texturas"] = {
            "cabeca": pygame.image.load("./src/" + skin["arquivos"]["cabeca"]),
            "corpo": pygame.image.load("./src/" + skin["arquivos"]["corpo"]),
            "fruta": pygame.image.load("./src/" + skin["arquivos"]["fruta"])
        }
    return SKINS[0]["texturas"]

def selecionar_skin(highscore, tela, LARGURA, ALTURA):
    selecionado = 0
    menu_desbloqueios(tela, highscore, LARGURA,ALTURA, selecionado)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return None
                elif evento.key == pygame.K_RETURN:
                    if highscore >= SKINS[selecionado]["highscore"]:
                        return SKINS[selecionado]["texturas"]
                elif evento.key == pygame.K_RIGHT and selecionado % 3 < 2:
                    selecionado += 1
                    menu_desbloqueios(tela, highscore, LARGURA, ALTURA, selecionado)
                elif evento.key == pygame.K_LEFT and selecionado % 3 > 0:
                    selecionado -= 1
                    menu_desbloqueios(tela, highscore, LARGURA, ALTURA, selecionado)
                elif evento.key == pygame.K_DOWN and selecionado < 3:
                    selecionado += 3
                    menu_desbloqueios(tela, highscore, LARGURA, ALTURA, selecionado)
                elif evento.key == pygame.K_UP and selecionado >= 3:
                    selecionado -= 3
                    menu_desbloqueios(tela, highscore, LARGURA, ALTURA, selecionado)

def menu_desbloqueios(tela, highscore, LARGURA, ALTURA, selecionado):

    tela.fill(PRETO)
    
    fonte = pygame.font.Font("./font/VCR.ttf", 32)
    titulo = fonte.render("Desbloqueios", True, BRANCO)
    tela.blit(titulo, (50, 20))

    largura_caixa = 100
    altura_caixa = 100
    espacamento = 50

    total_largura = 3 * largura_caixa + 2 * espacamento
    total_altura = 2 * altura_caixa + espacamento
    start_x = (LARGURA - total_largura) // 2
    start_y = (ALTURA - total_altura) // 2

    fonte = pygame.font.Font("./font/VCR.ttf", 16)
    fonte_negado = pygame.font.SysFont(None, 64)
    negado = fonte_negado.render("X", True, BRANCO)

    for i, skin in enumerate(SKINS):
        linha = i // 3
        coluna = i % 3
        x = start_x + coluna * (largura_caixa + espacamento)
        y = start_y + linha * (altura_caixa + espacamento)

        # Verifica se a skin está desbloqueada
        desbloqueada = highscore >= skin["highscore"]

        # Desenha a caixinha
        cor_caixa = VERDE if desbloqueada else CINZA
        pygame.draw.rect(tela, cor_caixa, (x, y, largura_caixa, altura_caixa))

        if i == selecionado:
            pygame.draw.rect(tela, BRANCO, (x-2, y-2, largura_caixa+4, altura_caixa+4), 3)

        if desbloqueada:
            tela.blit(skin["texturas"]["cabeca"], (x + 20, y + 20))
            tela.blit(skin["texturas"]["corpo"], (x + 20, y + 40))
            tela.blit(skin["texturas"]["corpo"], (x + 20, y + 60))
            tela.blit(skin["texturas"]["fruta"], (x + 60, y + 40))
        else:
            negado_rect = negado.get_rect(center=(x + largura_caixa//2, y + altura_caixa//2))
            tela.blit(negado, negado_rect)
            texto_preco = fonte.render(f"Score: {skin['highscore']}", True, BRANCO)
            preco_rect = texto_preco.get_rect(center=(x + largura_caixa//2, y + altura_caixa + 35))
            tela.blit(texto_preco, preco_rect)

        # Desenha o nome da skin
        texto_skin = fonte.render(skin["nome"], True, BRANCO)
        tela.blit(texto_skin, (x, y + altura_caixa + 10))

    pygame.display.flip()



