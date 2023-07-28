import pygame as pg
import pandas as pd
import data

window = pg.display.set_mode((1000, 700))
pg.font.init()
fonte = pg.font.SysFont("Courier New", 50, bold=True)

escondendo_numeros = True
tabuleiro_matriz_preenchido = True
click_last_status = False
click_x = -1
click_y = -1
numero = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        else:
            if event.type == pg.KEYDOWN:
                numero = pg.key.name(event.key)

    mouse = pg.mouse.get_pos()
    mouse_x = mouse[0]
    mouse_y = mouse[1]

    click = pg.mouse.get_pressed()

    #jogo
    data.monta_tabuleiro_matriz(window, mouse_x, mouse_y)
    click_position_x, click_position_y = data.seleciona_quadrado(window, mouse_x, mouse_y, click_last_status, click[0], click_x, click_y)
    data.desenha_tabuleiro_matriz(window)
    data.botao_reseta(window)
    tabuleiro_matriz, tabuleiro_matriz_preenchido = data.gabarito_tabuleiro_matriz(data.tabuleiro_matriz, tabuleiro_matriz_preenchido)
    jogo, escondendo_numeros = data.esconde_numeros(data.tabuleiro_matriz, data.jogo_matriz, escondendo_numeros)
    data.escreve_numeros(window, data.jogo_matriz)
    numero = data.digita_numero(numero)
    jogo, numero = data.checa_numero(window, data.tabuleiro_matriz, data.jogo_matriz, click_position_x, click_position_y, numero)
    tabuleiro_matriz_preenchido, escondendo_numeros, tabuleiro_matriz, jogo_matriz = data.clica_reseta(mouse_x, mouse_y, click_last_status, click[0], tabuleiro_matriz_preenchido, escondendo_numeros, data.tabuleiro_matriz, data.jogo_matriz)

    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()