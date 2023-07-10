#cuando creamos una variable dentro de una funcion, se dice que es una variable **local**, lo que significa que solo existe dentro de la funcion. #por ejemplo:

#en este caso la variable full_name, solo existe dentro de la funcion. la funcion tiene sus propias variables que no se filtran hacia afuera. en computacion a eso se le llama ambito o alcance. es decir, la variable full_name es de ambito local.
def say_hello(name, lastname):
  full_name = f"{name} {lastname}"    
  print(f"¡Hola {full_name}!")

say_hello("Lautaro", "Prieto")

#esto es un error, porque full_name solo existe dentro del ambito de la funcion say_hello
print(full_name)