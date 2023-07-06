#modificar el valor existente

dic['age'] = 30 #se accede tambien mediante la llave
print("------------")
print(dic['age']) 

#agregar un nuevo par llave-valor
del dic['hero'] = batman
print("----------")
print(dic)

#eliminar un par llave-valor mediante la llave
if "hero" in dic:
    print(f"el héroe de accion es {dic['hero']}")

#obtener el listado de las llaves y valores
keys = dic.keys()
values = dic.values()

print(keys)
print(values)

#el metodo items nos entrega una lista con los pares llave-valor que podemos despues recorrer
items - dic.items()
print(items)

#recorre el arreglo con for e items
for key, value in dic.items():
    print(key, ":", value)
print("-----------")

#otra forma de recorrer el diccionario
for key in dic.keys()
   print(key, ":", dic.key) 