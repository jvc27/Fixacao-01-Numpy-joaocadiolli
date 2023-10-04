import array_desaf

linha = '-----------------------------------------'
#Criar matriz(array_bi) 4x4. Origem: dados.txt
array_bi = array_desaf.array_bidimensional('dados.txt')

# Imprimir média da linha, coluna e matriz(array_bi)
print('Matriz 1:', array_bi, sep='\n', end='\n\n')
array_desaf.imprimir_medias(array_bi)

# Obter matriz(array_bi) transposta
matriz_trans = array_bi.transpose()
print('Matriz 1 trans:', matriz_trans, sep='\n')

print(linha)
print(linha)

# Criar matriz2(array2_bi)
array2_bi = array_desaf.array_bidimensional('dados2.txt')
print('Matriz 2:', array2_bi, sep='\n')

# Produto escalar entre matriz_trans(array_bi_trans) e matriz2(array2_bi)
print('Produto escalar entre matriz_trans e matriz2: ',
      array_desaf.produto_escalar(matriz_trans, array2_bi),
      sep='\n')

print(linha)
print(linha)

# Criar filtro para matriz
print(f'Filtro matriz:(n>10) {array_bi[array_bi>10]}')
print(f'Filtro matriz2:(n>10) {array2_bi[array2_bi>10]}')

print(linha)
print(linha)

# Operação matriz com matriz
print('Operação aritmética matriz com matriz.', end='\n\n')
array_desaf.operacao_arit(array_bi, array2_bi)
# Operação matriz com array
print('Operação aritmética array com matriz.', end='\n\n')
array_desaf.operacao_arit(array_desaf.np.array([1, 2, 3, 4]), array_bi)
