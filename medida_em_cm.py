# Ler uma medida em polegadas e imprimir a equivalente em centímetros, sabendo que 2.54 cm equivale a 1 polegada.

print('Digite uma medida em polegadas para ser convertida em centímetros:')
polegadas = float(input())
centimetros = polegadas * 2.54
print('A medida de {} polegadas equivale a {} centímetros.'.format(polegadas, centimetros))
