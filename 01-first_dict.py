# un diccionario es como una lista, pero mas general, es decir, en un diccionario los indices pueden ser casi de cualquier tipo.
#en los diccionarios los indices son llamados *llaves* o en ingles *keys* y tienen asociado sus respectivos valores

#ejemplo 
empty_dict = {} #crea un diccionario vacio

english_to_spanish = {"one":"uno","two":"dos"} #crea un diccionario con dos elementos

#los elementos se agregan en pares, es decir, llave-valor

english_to_spanish["hello"] = "hola"
english_to_spanish["bye"] = "chao"

print(english_to_spanish)

#para acceder a el valor de una llave en especifico usamos la notacion con []
print(english_to_spanish["one"])

#el largo de un diccionario se puede obtener con len(), igual en el las listas
print(len(english_to_spanish)) #=> 4