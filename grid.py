"""
Grade para imagem composta de caracteres

Suponha que você tenha uma lista de listas em que cada valor das listas internas seja uma string de um caractere como:

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]

Podemos pensar em grid[x][y] como sendo o caractere nas coordenadas x e y de uma “imagem” desenhada com caracteres textuais. A origem (0, 0) estará no canto superior esquerdo, as coordenadas x aumentam para a direita e as coordenadas y aumentam para baixo.

"""


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]




for i in range(len(grid[0])):
    for index in range(len(grid)):
        print(grid[index][i], end = '')

    print('')


        

