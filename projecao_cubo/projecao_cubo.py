import numpy as np
import pygame

def rotacao_matriz_x(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def rotacao_matriz_y(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def rotacao_matriz_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

def projecao(ponto):
    d = 2
    z = ponto[2] if ponto[2] != 0 else 0.01
    fator_escala = d / (d + z)
    return np.array([ponto[0] * fator_escala, ponto[1] * fator_escala])

def transformacao_aplicada(ponto, angulo_x, angulo_y, angulo_z, translacao):
    rotacionado = np.dot(rotacao_matriz_x(angulo_x), ponto)
    rotacionado = np.dot(rotacao_matriz_y(angulo_y), rotacionado)
    rotacionado = np.dot(rotacao_matriz_z(angulo_z), rotacionado)
    return rotacionado + translacao

def desenhar(tela, vertices, arestas, angulo_x, angulo_y, angulo_z, translacao):
    vertices_projetados = []
    for vertice in vertices:
        transformado = transformacao_aplicada(vertice, angulo_x, angulo_y, angulo_z, translacao)
        projetado = projecao(transformado)
        ajustado = projetado * 200 + np.array([300, 300])
        vertices_projetados.append(ajustado)
    for aresta in arestas:
        pygame.draw.line(tela, (255, 255, 100), vertices_projetados[aresta[0]], vertices_projetados[aresta[1]], 2)
    for vertice in vertices_projetados:
        pygame.draw.rect(tela, (255, 255, 100), (vertice[0] - 3, vertice[1] - 3, 6, 6))

def main():
    pygame.init()
    tela = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Cubo")
    relogio = pygame.time.Clock()


    vertices = np.array([
        [-1, -1, -1], [-1, -1,  1], [-1,  1, -1], [-1,  1,  1],
        [ 1, -1, -1], [ 1, -1,  1], [ 1,  1, -1], [ 1,  1,  1]
    ])

    arestas = [(0, 1), (1, 3), (3, 2), (2, 0), (4, 5), (5, 7), (7, 6), (6, 4), 
               (0, 4), (1, 5), (2, 6), (3, 7)]

    angulo_x = angulo_y = angulo_z = 0
    velocidade_x = velocidade_y = velocidade_z = 0.01
    translacao = np.array([0, 0, -8])
    forma_atual = "cubo"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            velocidade_x += 0.01
            velocidade_y += 0.01
            velocidade_z += 0.01
        if teclas[pygame.K_LEFT]:
            velocidade_x -= 0.01
            velocidade_y -= 0.01
            velocidade_z -= 0.01
        if teclas[pygame.K_c]:
            forma_atual = "cubo"

        angulo_x += velocidade_x
        angulo_y += velocidade_y
        angulo_z += velocidade_z

        tela.fill((0, 0, 0))
        if forma_atual == "cubo":
            desenhar(tela, vertices, arestas, angulo_x, angulo_y, angulo_z, translacao)

        pygame.display.flip()
        relogio.tick(60)

if __name__ == "__main__":
    main()
