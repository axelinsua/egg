'''ARRAYS 1D PARTE 1: 
1. Crea un array_1 lleno ceros con una longitud de 8 elementos. 
2. Haz que todos los elementos de este array sean igual a 2 
3. Crea un array_2 que contenga todos los números pares del 1 al 10.
4. Suma todos los elementos del array_2 usando un bucle y después usando un método 
de numpy. Compara los resultados
5. Revierte array_2 y guárdalo en una variable independiente. 
6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y 
array_2_revertido 
 (Pista: Investiga el uso de intersect1d() de numpy)
7. Crea un arrays lleno de 1s con una longitud dada por el usuario
'''
from functools import reduce as rd
import numpy as np
array=np.zeros(8)
array.fill(2)
array_2=np.arange(2,11,2)

suma=0
for i in range(len(array_2)):
    suma+=array_2[i]
suma_2= sum(array_2)
array_3=array_2.copy()
array_3=np.flip(array_3)



#inter= np.intersect1d(array, array_2)
intersection=rd(np.intersect1d, (array_2,array_3, array))

print(intersection)
print(array)
print(array_2)
print(suma,'\n',suma_2)
print(array_3)

#7 
long=int(input('escriba la longitud del array \n'))
arr=np.ones(long)
print(arr)