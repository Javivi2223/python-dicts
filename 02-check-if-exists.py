english_to_spanish = {"one":"uno","two":"dos"} #crea un diccionario con dos elementos

#podemos revisar si cierta llave esta presente en el diccionario con la palabra reservada in

if "one" in english_to_spanish:
    print("si esta la llave one")
    print("su valor es:", english_to_spanish["one"])

#si tratamos de acceder a una llave q no existe, cometeremos un error de llave

#print(english_to_spanish[three])