# crie um programa que leia data.csv e exiba seu índice e conteúdo na tela
# dica: use enumerate()
# dica: use open() e .readlines()
# dica: use print() e .format()
# dica: use for
# dica: use split()
import csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        print('Linha {}: {}'.format(i, row))
        # crie um arquivo .py para cada índice e escreva um comentário com seu conteúdo
        # dica: use open() e .write()
        # dica: use .format()
        # dica: use open() e .close()
        with open('{}.py'.format(i), 'w') as f2:
            f2.write('# {}'.format(row))
            f2.close()
        i += 1
