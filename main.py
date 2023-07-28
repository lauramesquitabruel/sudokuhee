import pygame as pg
import pandas as pd
import random
import math 

window = pg.display.set_mode((1000, 700))
pg.font.init()
fonte = pg.font.SysFont("Courier New", 50, bold=True)

preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azulclaro = (200,200,255)
azul = (100,100,255)
branco = (255,255,255)

tabuleiro = [
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ]
    ]

jogo = [
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ],
    ["n", "n", "n", "n", "n", "n", "n", "n", "n", ]
    ]

def monta_tabuleiro(window, mouse_x, mouse_y):
    quadrado = 66.7
    ajuste = 50
    x = (math.ceil((mouse_x - ajuste) / quadrado) - 1)
    y = (math.ceil((mouse_y - ajuste) / quadrado) - 1)
    pg.draw.rect(window, branco, (0, 0, 1000, 700))
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, azulclaro, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))

def seleciona_quadrado(window, mouse_x, mouse_y, click_last_status, click, x, y):
    quadrado = 66.7
    ajuste = 50
    if click_last_status == True and click == True:
        x = (math.ceil((mouse_x - ajuste) / quadrado) - 1)
        y = (math.ceil((mouse_y - ajuste) / quadrado) - 1)
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, azul, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))
    return x, y

def desenha_tabuleiro(window):
    pg.draw.rect(window, preto, (50, 50, 600, 600), 6)
    pg.draw.rect(window, preto, (50, 250, 600, 200), 6)
    pg.draw.rect(window, preto, (250, 50, 200, 600), 6)
    pg.draw.rect(window, preto, (50, 117, 600, 67), 2)
    pg.draw.rect(window, preto, (50, 317, 600, 67), 2)
    pg.draw.rect(window, preto, (50, 517, 600, 67), 2)
    pg.draw.rect(window, preto, (117, 50, 67, 600), 2)
    pg.draw.rect(window, preto, (317, 50, 67, 600), 2)
    pg.draw.rect(window, preto, (517, 50, 67, 600), 2)

def botao_reseta(window):
    pg.draw.rect(window, verde, (700, 50, 250, 100))
    palavra_f = fonte.render('Restart', True, preto)
    window.blit(palavra_f, (725, 75))

def linha_escolhida(tabuleiro, y):
    linha_sorteada = tabuleiro[y]
    return linha_sorteada

def coluna_escolhida(tabuleiro, x):
    coluna_sorteada = []
    for n in range(8):
        coluna_sorteada.append(tabuleiro[n][x])
    return coluna_sorteada

def quadrante_selecionado(tabuleiro, x, y):
    quadrante = []
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2],
                          tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2],
                          tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]])
    elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro[0][3], tabuleiro[0][4], tabuleiro[0][5],
                          tabuleiro[1][3], tabuleiro[1][4], tabuleiro[1][5],
                          tabuleiro[2][3], tabuleiro[2][4], tabuleiro[2][5]])
    elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro[0][6], tabuleiro[0][7], tabuleiro[0][8],
                          tabuleiro[1][6], tabuleiro[1][7], tabuleiro[1][8],
                          tabuleiro[2][6], tabuleiro[2][7], tabuleiro[2][8]])
    elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro[3][0], tabuleiro[3][1], tabuleiro[3][2],
                          tabuleiro[4][0], tabuleiro[4][1], tabuleiro[4][2],
                          tabuleiro[5][0], tabuleiro[5][1], tabuleiro[5][2]])
    elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro[3][3], tabuleiro[3][4], tabuleiro[3][5],
                          tabuleiro[4][3], tabuleiro[4][4], tabuleiro[4][5],
                          tabuleiro[5][3], tabuleiro[5][4], tabuleiro[5][5]])
    elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro[3][6], tabuleiro[3][7], tabuleiro[3][8],
                          tabuleiro[4][6], tabuleiro[4][7], tabuleiro[4][8],
                          tabuleiro[5][6], tabuleiro[5][7], tabuleiro[5][8]])
    elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro[6][0], tabuleiro[6][1], tabuleiro[6][2],
                          tabuleiro[7][0], tabuleiro[7][1], tabuleiro[7][2],
                          tabuleiro[8][0], tabuleiro[8][1], tabuleiro[8][2]])
    elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro[6][3], tabuleiro[6][4], tabuleiro[6][5],
                          tabuleiro[7][3], tabuleiro[7][4], tabuleiro[7][5],
                          tabuleiro[8][3], tabuleiro[8][4], tabuleiro[8][5]])
    elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro[6][6], tabuleiro[6][7], tabuleiro[6][8],
                          tabuleiro[7][6], tabuleiro[7][7], tabuleiro[7][8],
                          tabuleiro[8][6], tabuleiro[8][7], tabuleiro[8][8]])
    return quadrante

def preenchendo_quadrantes(tabuleiro, x2, y2):
    quadrante_preenchido = True
    loop = 0
    try_count = 0
    numero = 1
    while quadrante_preenchido == True:
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
        linha_sorteada = linha_escolhida(tabuleiro, y)
        coluna_sorteada = coluna_escolhida(tabuleiro, x)
        quadrante = quadrante_selecionado(tabuleiro, x, y)
        if tabuleiro[y][x] == 'n' and numero not in linha_sorteada and numero not in coluna_sorteada and numero not in quadrante:
            tabuleiro[y][x] = numero
            numero += 1
        loop += 1
        if loop == 50:
            tabuleiro[y2][x2] = 'n'
            tabuleiro[y2][x2 + 1] = 'n'
            tabuleiro[y2][x2 + 2] = 'n'
            tabuleiro[y2 + 1][x2] = 'n'
            tabuleiro[y2 + 1][x2 + 1] = 'n'
            tabuleiro[y2 + 1][x2 + 2] = 'n'
            tabuleiro[y2 + 2][x2] = 'n'
            tabuleiro[y2 + 2][x2 + 1] = 'n'
            tabuleiro[y2 + 2][x2 + 2] = 'n'
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
    return tabuleiro

def reinicia_tabuleiro(tabuleiro):
    tabuleiro = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
    return tabuleiro

def gabarito_tabuleiro(tabuleiro, tabuleiro_preenchido):
    while tabuleiro_preenchido == True:
        # Quadrante 1
        tabuleiro = preenchendo_quadrantes(tabuleiro, 0, 0)
        # Quadrante 2
        tabuleiro = preenchendo_quadrantes(tabuleiro, 3, 0)
        # Quadrante 3
        tabuleiro = preenchendo_quadrantes(tabuleiro, 6, 0)
        # Quadrante 4
        tabuleiro = preenchendo_quadrantes(tabuleiro, 0, 3)
        # Quadrante 7
        tabuleiro = preenchendo_quadrantes(tabuleiro, 0, 6)
        # Quadrante 5
        tabuleiro = preenchendo_quadrantes(tabuleiro, 3, 3)
        # Quadrante 8
        tabuleiro = preenchendo_quadrantes(tabuleiro, 3, 6)
        # Quadrante 6
        tabuleiro = preenchendo_quadrantes(tabuleiro, 6, 3)
        # Quadrante 9
        tabuleiro = preenchendo_quadrantes(tabuleiro, 6, 6)
        for nn in range(9):
            for n in range(9):
                if tabuleiro[nn][n] == 'n':
                    tabuleiro = reinicia_tabuleiro(tabuleiro)
        count = 0
        for nn in range(9):
            for n in range(9):
                if tabuleiro[nn][n] != 'n':
                    count += 1
        if count == 81:
            tabuleiro_preenchido = False
    return tabuleiro, tabuleiro_preenchido

def esconde_numeros(tabuleiro, jogo, escondendo_numeros):
    if escondendo_numeros == True:
        for n in range(40):
            sorteando_numero = True
            while sorteando_numero == True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if jogo[y][x] == 'n':
                    jogo[y][x] = tabuleiro[y][x]
                    sorteando_numero = False
        escondendo_numeros = False
    return jogo, escondendo_numeros

def escreve_numeros(window, jogo):
    quadrado = 66.7
    ajuste = 67
    for nn in range(9):
        for n in range(9):
            if jogo[nn][n] != 'n':
                palavra = fonte.render(str(jogo[nn][n]), True, preto)
                window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))
                if jogo[nn][n] == 'X':
                    palavra = fonte.render(str(jogo[nn][n]), True, vermelho)
                    window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))

def digita_numero(numero):
    try:
        numero = int(numero[1])
    except:
        numero = int(numero)
    return numero

def checa_numero(window, tabuleiro, jogo, click_position_x, click_position_y, numero):
    x = click_position_x
    y = click_position_y
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro[y][x] == numero and jogo[y][x] == 'n' and numero != 0:
        jogo[y][x] = numero
        numero = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro[y][x] == numero and jogo[y][x] == numero and numero != 0:
        pass
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro[y][x] != numero and jogo[y][x] == 'n' and numero != 0:
        jogo[y][x] = 'X'
        numero = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro[y][x] == numero and jogo[y][x] == 'X' and numero != 0:
        jogo[y][x] = numero
        numero = 0
    return jogo, numero

def clica_reseta(mouse_position_x, mouse_position_y, click_last_status, click, tabuleiro_preenchido, escondendo_numeros, tabuleiro, jogo):
    x = mouse_position_x
    y = mouse_position_y
    if x >= 700 and x <= 950 and y >= 50 and y <= 150 and click_last_status == False and click == True:
        tabuleiro_preenchido = True
        escondendo_numeros = True
        tabuleiro = reinicia_tabuleiro(tabuleiro)
        jogo = reinicia_tabuleiro(jogo)
    return tabuleiro_preenchido, escondendo_numeros, tabuleiro, jogo

escondendo_numeros = True
tabuleiro_preenchido = True
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
    monta_tabuleiro(window, mouse_x, mouse_y)
    click_position_x, click_position_y = seleciona_quadrado(window, mouse_x, mouse_y, click_last_status, click[0], click_x, click_y)
    desenha_tabuleiro(window)
    botao_reseta(window)
    tabuleiro, tabuleiro_preenchido = gabarito_tabuleiro(tabuleiro, tabuleiro_preenchido)
    jogo, escondendo_numeros = esconde_numeros(tabuleiro, jogo, escondendo_numeros)
    escreve_numeros(window, jogo)
    numero = digita_numero(numero)
    jogo, numero = checa_numero(window, tabuleiro, jogo, click_position_x, click_position_y, numero)
    tabuleiro_preenchido, escondendo_numeros, tabuleiro, jogo = clica_reseta(mouse_x, mouse_y, click_last_status, click[0], tabuleiro_preenchido, escondendo_numeros, tabuleiro, jogo)

    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()