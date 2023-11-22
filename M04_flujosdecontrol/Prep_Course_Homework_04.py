#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
a = 8

if a>0:
    print('El valor de la variable "A" es > a 0')
else:
    print('El valor de la variable "A" es <= a 0') 




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
a = 3
b = 5

if type(a) == type(b):
    print('Las variables "A" y "B" son del mismo tipo')
else:
    print('Las variables "A" y "B" son de diferente tipo')



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for i in range(1, 21):
  if (i % 2) == 0:
    print(str(i)+' es un número par')
  else:
    print(str(i)+' es un número impar')




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(6):
    print(i**3)



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
a = 7

for i in range(a):
    print(i+1)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
a = 4
fact=1

if a>0:
  b = a
  while b>1:
    fact *= b
    b -= 1
print('El factorial de '+str(a)+' es: '+str(fact))


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
while True:
  for i in range(10):
    print('Queda ',10-i)
  break




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
for i in range(6):
  a = i+1
  print('Iteración ', a)
  while a> 0:
    print('Valgo ', a)
    a -= 1




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

for i in range(1, 31):
  a = 0
  for j in range(1, i):
    if (i % j) == 0:
      a += 1
  if a < 2:
    print(str(i)+' es un número primo')


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
for i in range(2, 31):
    a = 0
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            a += 1
            break
    else:
        print(str(i) + ' es un número primo')



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

for i in range(2, 31):
    a = 0
    pasos = 0
    for j in range(2, int(i**0.5) + 1):
        pasos += 1
        if i % j == 0:
            a += 1
            break
    else:
        print(f"{i} es un número primo. Pasos: {pasos}")



# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

numero = 100

while numero <= 300:
    if numero % 12 != 0:
        numero += 1
        continue
    print(numero)
    numero += 1




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_siguiente_primo(numero_actual):
    siguiente_numero = numero_actual + 1
    while True:
        if es_primo(siguiente_numero):
            return siguiente_numero
        siguiente_numero += 1

while True:
    entrada_usuario = input("Ingresa un número para verificar si es primo (o 'salir' para salir): ")

    if entrada_usuario.lower() == 'salir':
        break

    try:
        numero = int(entrada_usuario)
        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
        
        buscar_siguiente = input("¿Quieres buscar el siguiente número primo? (s/n): ")
        if buscar_siguiente.lower() != 's':
            break

        numero = encontrar_siguiente_primo(numero)
        print(f"El siguiente número primo es: {numero}")

    except ValueError:
        print("Por favor, ingresa un número entero válido.")



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

numero = 100

while numero <= 300:
    if numero % 3 != 0 or numero % 6 != 0:
        numero += 1
        continue
    print(f"El primer número divisible por 3 y múltiplo de 6 en el rango de 100 a 300 es: {numero}")
    break


