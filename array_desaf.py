import numpy as np


def array_bidimensional(nome_do_arquivo):
  array = np.genfromtxt(nome_do_arquivo,
                        delimiter=';',
                        dtype=int,
                        skip_header=1)
  return array.reshape(4, -1)


def imprimir_medias(array_bi):
  print('Média das linhas:',
        array_bi.mean(axis=1),
        'Média das colunas:',
        array_bi.mean(axis=0),
        'Média da matriz:',
        array_bi.mean(),
        sep='\n',
        end='\n\n')


def produto_escalar(array_bi, array2_bi):
  return np.dot(array_bi, array2_bi)


def operacao_arit(array, array2):
  print('Adição:', array + array2, sep='\n', end='\n\n')
  print('Divisão:', array / array2, sep='\n', end='\n\n')
  print('Subtração:', array - array2, sep='\n', end='\n\n')
