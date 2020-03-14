import numpy as np

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])

soma = a + b
subtracao = a - b
produto = a * b 
quociente = a / b

print('Soma: \n', + soma)
print('\n')
print('Diferença: \n', + subtracao)
print('\n')
print('Produto: \n', + produto)
print('\n')
print('Quociente: \n', + quociente)








print('\n')
produto_matricial = a.dot(b) 
 
print('Produto Matricial: \n', + produto_matricial)
