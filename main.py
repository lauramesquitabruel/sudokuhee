import pygame as pg
import pandas as pd
import random
import math 
import data

window = pg.display.set_mode((1000, 700))
pg.font.init()
fonte = pg.font.SysFont("Courier New", 50, bold=True)

def monta_tabuleiro_matriz(window, mouse_x, mouse_y):
    quadrado = 66.7
    ajuste = 50
    x = (math.ceil((mouse_x - ajuste) / quadrado) - 1)
    y = (math.ceil((mouse_y - ajuste) / quadrado) - 1)
    pg.draw.rect(window, data.branco, (0, 0, 1000, 700))
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, data.azulclaro, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))

def seleciona_quadrado(window, mouse_x, mouse_y, click_last_status, click, x, y):
    quadrado = 66.7
    ajuste = 50
    if click_last_status == True and click == True:
        x = (math.ceil((mouse_x - ajuste) / quadrado) - 1)
        y = (math.ceil((mouse_y - ajuste) / quadrado) - 1)
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, data.azul, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))
    return x, y

def desenha_tabuleiro_matriz(window):
    pg.draw.rect(window, data.preto, (50, 50, 600, 600), 6)
    pg.draw.rect(window, data.preto, (50, 250, 600, 200), 6)
    pg.draw.rect(window, data.preto, (250, 50, 200, 600), 6)
    pg.draw.rect(window, data.preto, (50, 117, 600, 67), 2)
    pg.draw.rect(window, data.preto, (50, 317, 600, 67), 2)
    pg.draw.rect(window, data.preto, (50, 517, 600, 67), 2)
    pg.draw.rect(window, data.preto, (117, 50, 67, 600), 2)
    pg.draw.rect(window, data.preto, (317, 50, 67, 600), 2)
    pg.draw.rect(window, data.preto, (517, 50, 67, 600), 2)

def botao_reseta(window):
    pg.draw.rect(window, data.verde, (700, 50, 250, 100))
    palavra_f = fonte.render('Restart', True, data.preto)
    window.blit(palavra_f, (725, 75))

def linha_escolhida(tabuleiro_matriz, y):
    linha_sorteada = tabuleiro_matriz[y]
    return linha_sorteada

def coluna_escolhida(tabuleiro_matriz, x):
    coluna_sorteada = []
    for n in range(8):
        coluna_sorteada.append(tabuleiro_matriz[n][x])
    return coluna_sorteada

def quadrante_selecionado(tabuleiro_matriz, x, y):
    quadrante = []
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro_matriz[0][0], tabuleiro_matriz[0][1], tabuleiro_matriz[0][2],
                          tabuleiro_matriz[1][0], tabuleiro_matriz[1][1], tabuleiro_matriz[1][2],
                          tabuleiro_matriz[2][0], tabuleiro_matriz[2][1], tabuleiro_matriz[2][2]])
    elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro_matriz[0][3], tabuleiro_matriz[0][4], tabuleiro_matriz[0][5],
                          tabuleiro_matriz[1][3], tabuleiro_matriz[1][4], tabuleiro_matriz[1][5],
                          tabuleiro_matriz[2][3], tabuleiro_matriz[2][4], tabuleiro_matriz[2][5]])
    elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro_matriz[0][6], tabuleiro_matriz[0][7], tabuleiro_matriz[0][8],
                          tabuleiro_matriz[1][6], tabuleiro_matriz[1][7], tabuleiro_matriz[1][8],
                          tabuleiro_matriz[2][6], tabuleiro_matriz[2][7], tabuleiro_matriz[2][8]])
    elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro_matriz[3][0], tabuleiro_matriz[3][1], tabuleiro_matriz[3][2],
                          tabuleiro_matriz[4][0], tabuleiro_matriz[4][1], tabuleiro_matriz[4][2],
                          tabuleiro_matriz[5][0], tabuleiro_matriz[5][1], tabuleiro_matriz[5][2]])
    elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro_matriz[3][3], tabuleiro_matriz[3][4], tabuleiro_matriz[3][5],
                          tabuleiro_matriz[4][3], tabuleiro_matriz[4][4], tabuleiro_matriz[4][5],
                          tabuleiro_matriz[5][3], tabuleiro_matriz[5][4], tabuleiro_matriz[5][5]])
    elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro_matriz[3][6], tabuleiro_matriz[3][7], tabuleiro_matriz[3][8],
                          tabuleiro_matriz[4][6], tabuleiro_matriz[4][7], tabuleiro_matriz[4][8],
                          tabuleiro_matriz[5][6], tabuleiro_matriz[5][7], tabuleiro_matriz[5][8]])
    elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro_matriz[6][0], tabuleiro_matriz[6][1], tabuleiro_matriz[6][2],
                          tabuleiro_matriz[7][0], tabuleiro_matriz[7][1], tabuleiro_matriz[7][2],
                          tabuleiro_matriz[8][0], tabuleiro_matriz[8][1], tabuleiro_matriz[8][2]])
    elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro_matriz[6][3], tabuleiro_matriz[6][4], tabuleiro_matriz[6][5],
                          tabuleiro_matriz[7][3], tabuleiro_matriz[7][4], tabuleiro_matriz[7][5],
                          tabuleiro_matriz[8][3], tabuleiro_matriz[8][4], tabuleiro_matriz[8][5]])
    elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro_matriz[6][6], tabuleiro_matriz[6][7], tabuleiro_matriz[6][8],
                          tabuleiro_matriz[7][6], tabuleiro_matriz[7][7], tabuleiro_matriz[7][8],
                          tabuleiro_matriz[8][6], tabuleiro_matriz[8][7], tabuleiro_matriz[8][8]])
    return quadrante

def preenchendo_quadrantes(tabuleiro_matriz, x2, y2):
    quadrante_preenchido = True
    loop = 0
    try_count = 0
    numero = 1
    while quadrante_preenchido == True:
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
        linha_sorteada = linha_escolhida(tabuleiro_matriz, y)
        coluna_sorteada = coluna_escolhida(tabuleiro_matriz, x)
        quadrante = quadrante_selecionado(tabuleiro_matriz, x, y)
        if tabuleiro_matriz[y][x] == 'n' and numero not in linha_sorteada and numero not in coluna_sorteada and numero not in quadrante:
            tabuleiro_matriz[y][x] = numero
            numero += 1
        loop += 1
        if loop == 50:
            tabuleiro_matriz[y2][x2] = 'n'
            tabuleiro_matriz[y2][x2 + 1] = 'n'
            tabuleiro_matriz[y2][x2 + 2] = 'n'
            tabuleiro_matriz[y2 + 1][x2] = 'n'
            tabuleiro_matriz[y2 + 1][x2 + 1] = 'n'
            tabuleiro_matriz[y2 + 1][x2 + 2] = 'n'
            tabuleiro_matriz[y2 + 2][x2] = 'n'
            tabuleiro_matriz[y2 + 2][x2 + 1] = 'n'
            tabuleiro_matriz[y2 + 2][x2 + 2] = 'n'
            loop = 0
            numero = 1
            try_count += 1
        if try_count == 10:
            break
        count = 0
        for n in range(9):
            if quadrante[n] != 'n':
                count += 1
        if count == 9:
            quadrante_preenchido = False
    return tabuleiro_matriz

def reinicia_tabuleiro_matriz(tabuleiro_matriz):
    tabuleiro_matriz = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
    return tabuleiro_matriz

def gabarito_tabuleiro_matriz(tabuleiro_matriz, tabuleiro_matriz_preenchido):
    while tabuleiro_matriz_preenchido == True:
        # Quadrante 1
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 0, 0)
        # Quadrante 2
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 3, 0)
        # Quadrante 3
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 6, 0)
        # Quadrante 4
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 0, 3)
        # Quadrante 7
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 0, 6)
        # Quadrante 5
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 3, 3)
        # Quadrante 8
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 3, 6)
        # Quadrante 6
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 6, 3)
        # Quadrante 9
        tabuleiro_matriz = preenchendo_quadrantes(tabuleiro_matriz, 6, 6)
        for nn in range(9):
            for n in range(9):
                if tabuleiro_matriz[nn][n] == 'n':
                    tabuleiro_matriz = reinicia_tabuleiro_matriz(tabuleiro_matriz)
        count = 0
        for nn in range(9):
            for n in range(9):
                if tabuleiro_matriz[nn][n] != 'n':
                    count += 1
        if count == 81:
            tabuleiro_matriz_preenchido = False
    return tabuleiro_matriz, tabuleiro_matriz_preenchido

def esconde_numeros(tabuleiro_matriz, jogo_matriz, escondendo_numeros):
    if escondendo_numeros == True:
        for n in range(40):
            sorteando_numero = True
            while sorteando_numero == True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if jogo_matriz[y][x] == 'n':
                    jogo_matriz[y][x] = tabuleiro_matriz[y][x]
                    sorteando_numero = False
        escondendo_numeros = False
    return jogo_matriz, escondendo_numeros

def escreve_numeros(window, jogo_matriz):
    quadrado = 66.7
    ajuste = 67
    for nn in range(9):
        for n in range(9):
            if jogo_matriz[nn][n] != 'n':
                palavra = fonte.render(str(jogo_matriz[nn][n]), True, data.preto)
                window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))
                if jogo_matriz[nn][n] == 'X':
                    palavra = fonte.render(str(jogo_matriz[nn][n]), True, data.vermelho)
                    window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))

def digita_numero(numero):
    try:
        numero = int(numero[1])
    except:
        numero = int(numero)
    return numero

def checa_numero(window, tabuleiro_matriz, jogo_matriz, click_position_x, click_position_y, numero):
    x = click_position_x
    y = click_position_y
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro_matriz[y][x] == numero and jogo_matriz[y][x] == 'n' and numero != 0:
        jogo_matriz[y][x] = numero
        numero = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro_matriz[y][x] == numero and jogo_matriz[y][x] == numero and numero != 0:
        pass
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro_matriz[y][x] != numero and jogo_matriz[y][x] == 'n' and numero != 0:
        jogo_matriz[y][x] = 'X'
        numero = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro_matriz[y][x] == numero and jogo[y][x] == 'X' and numero != 0:
        jogo_matriz[y][x] = numero
        numero = 0
    return jogo, numero

def clica_reseta(mouse_position_x, mouse_position_y, click_last_status, click, tabuleiro_matriz_preenchido, escondendo_numeros, tabuleiro_matriz, jogo_matriz):
    x = mouse_position_x
    y = mouse_position_y
    if x >= 700 and x <= 950 and y >= 50 and y <= 150 and click_last_status == False and click == True:
        tabuleiro_matriz_preenchido = True
        escondendo_numeros = True
        tabuleiro_matriz = reinicia_tabuleiro_matriz(tabuleiro_matriz)
        jogo_matriz = reinicia_tabuleiro_matriz(jogo_matriz)
    return tabuleiro_matriz_preenchido, escondendo_numeros, tabuleiro_matriz, jogo_matriz

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
    monta_tabuleiro_matriz(window, mouse_x, mouse_y)
    click_position_x, click_position_y = seleciona_quadrado(window, mouse_x, mouse_y, click_last_status, click[0], click_x, click_y)
    desenha_tabuleiro_matriz(window)
    botao_reseta(window)
    tabuleiro_matriz, tabuleiro_matriz_preenchido = gabarito_tabuleiro_matriz(data.tabuleiro_matriz, tabuleiro_matriz_preenchido)
    jogo, escondendo_numeros = esconde_numeros(data.tabuleiro_matriz, data.jogo_matriz, escondendo_numeros)
    escreve_numeros(window, data.jogo_matriz)
    numero = digita_numero(numero)
    jogo, numero = checa_numero(window, data.tabuleiro_matriz, data.jogo_matriz, click_position_x, click_position_y, numero)
    tabuleiro_matriz_preenchido, escondendo_numeros, tabuleiro_matriz, jogo_matriz = clica_reseta(mouse_x, mouse_y, click_last_status, click[0], tabuleiro_matriz_preenchido, escondendo_numeros, data.tabuleiro_matriz, data.jogo_matriz)

    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()