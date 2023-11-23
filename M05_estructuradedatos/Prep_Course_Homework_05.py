#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
paises = ['Venezuela', 'Bolivía', 'Colombia', 'Ecuador', 'Peru']
print(paises)



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print('El segundo elemento de la lista de países es: ', paises[1])



# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print('Estos son los elementos del 2 al 4: ', paises[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:

print('El tipo de dato es: ', type(paises))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(paises[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(paises[:4])

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

paises.append('Uruguay')
paises.append('Venezuela')
print(paises)
# no arroja error, los agrega sin problema





# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

paises.insert(3, 'Paraguay')
print(paises)


# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

paises_2 = ['Chile', 'Brasil', 'Argentina']
paises.extend(paises_2)
print(paises)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

print(paises.index('Venezuela'))



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

# da un error 



# 12) Eliminar un elemento de la lista

# In[25]:

paises.pop()
print(paises)


# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

paises.pop(7)
print(paises)



# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:


ultimo_elemento = paises.pop()
print(ultimo_elemento)


# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(paises*4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

lista = []
for i in range(20):
    lista.append(i+1)
dupla = tuple(lista)
print(dupla)

# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(dupla[11:16])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

if dupla in [20, 30]:
  print('Los números 20 y 30 están dentro de la dupla.')
else:
  print('Los números 20 y 30 no están dentro de la dupla.')



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

elemento = 'Paris'
if elemento not in paises:
  paises.append(elemento)
print(paises)

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

for l in paises:
  print(l+' está '+str(paises.count(l))+' veces')

for d in dupla:
  print(str(d)+' está '+str(paises.count(d))+' veces')

# 21) Convertir la tupla en una lista

# In[52]:

lista = list(dupla)
print(lista)



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

a, b, c = dupla[:3]
print(a, b, c)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

pais = {
  'pais': paises,
  'ciudad': ['Mérida', 'Barinas', 'Zulia', 'Falcón'],
  'continente': 'America'
}
print(pais)



# 24) Imprimir las claves del diccionario

# In[59]:

for k in pais.keys():
  print(k)


# 25) Imprimir las ciudades a través de su clave

# In[61]:

for k in pais.keys():
  print(pais[k])


