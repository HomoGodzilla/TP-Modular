import pygame
import Skins
from Menu import Menu
from Game import Game

def carregar_configuracoes():
    with open('settings.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        LARGURA = int(linhas[0].split(" ")[1])
        ALTURA = int(linhas[1].split(" ")[1])
        SCORE = int(linhas[2].split(" ")[1])
    return LARGURA, ALTURA, SCORE

def atualizar_highscore(novo_highscore):
    with open("settings.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    linhas[2] = f"Highscore {novo_highscore}\n"

    with open("settings.txt", "w") as arquivo:
        arquivo.writelines(linhas)

def main():
    LARGURA, ALTURA, SCORE = carregar_configuracoes()
    last_score = SCORE
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo da Cobrinha")
    clock = pygame.time.Clock()
    skin_selecionada = Skins.carregar_skins()

    menu = Menu(LARGURA, ALTURA)
    em_menu = True

    while em_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                em_menu = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    menu.mover_selecao("UP")
                elif evento.key == pygame.K_DOWN:
                    menu.mover_selecao("DOWN")
                elif evento.key == pygame.K_RETURN:
                    opcao = menu.selecionar()
                    if opcao == "JOGAR":
                        jogo = Game(LARGURA, ALTURA, SCORE,skin_selecionada)
                        last_score=jogo.loop_principal()
                    elif opcao == "SKINS":
                        skin_selecionada = Skins.selecionar_skin(SCORE,tela,LARGURA,ALTURA)
                    elif opcao == "SAIR":
                        em_menu = False
        if last_score>SCORE:
            atualizar_highscore(last_score)
            SCORE = last_score
        menu.desenhar_menu(tela)
        pygame.display.update()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()