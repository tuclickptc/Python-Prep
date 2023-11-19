#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
valor = 8
print(valor)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(valor))




# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre = 'Jorge Ortega'
print('Mi nombre es ', nombre)


# 5) Crear una variable que contenga un número complejo

# In[3]:
valor1 = 5 + 3j
print(valor1)



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(valor1))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
pi = 3.1416
valor2 = round(pi, 4)
print(valor2)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
"""
   Las variables son diferentes ya que son de diferente tipo.
"""
valor3 = 'True'
valor4 = True




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print('El tipo de la variable 3 es: ',type(valor3),' y el tipo de la variable 4 es: ',type(valor4))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
valor5 = 8 + 3.2
print(valor5)



# 11) Realizar una operación de suma de números complejos

# In[2]:
valor6 = 4 + 2j
valor7 = 6 + 5j
resultado = valor6 + valor7
print(resultado)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
resultado1 = 8 + (3 + 4j)
print(resultado1)



# 13) Realizar una operación de multiplicación

# In[5]:
resultado2 = 4 * 2
print(resultado2)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
resultado3 = 2**8
print(resultado3)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
division = 27/4
print(division)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
entero = 27//4
print(entero)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
resto = 27 % 4
print(resto)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
resultado4 = 4*entero + resto
print(resultado4)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
nombre = 'Jorge'
apellido = 'Ortega'
nombreCompleto = nombre + ' ' + apellido
print(nombreCompleto)



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
bool('2' == 2)
"""
    No son igual, porque el '2' es un string y el otro es un número.
"""




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
bool('2' == str(2))




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
"""
   Porque el dato es una cadena, debe tener un punto para que lo tome como flotante.
"""



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
valor8 = 3
valor8 -= 1
print(valor8)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
valor9 = 1 << 2
"""
   El sistema binario solo tiene en cuenta el 0 y el 1, el resultado da 4 ya que desplaza 2 posiciones a la izquierda al número 1, quedando 100 en el sistema binario.
"""



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
"""
   Da error ya que se están sumando variables de diferentes tipo, si fueran variables del mismo tipo no habría problema.
"""
# a = '2' + 2


# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
cadena = 'Cantemos todos'
valor10 = 4
print((cadena+' ')*valor10+', he repetido "'+cadena+'" '+str(valor10)+' veces')

