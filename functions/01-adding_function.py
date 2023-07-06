#en el contexto de la programacion las funciones son una secuencia de sentencias de codigo con un nombre.
#se parecen en algo a las variables en el sentido que son un simple nombre. en el caso de las variables, estas apuntan a un valor, mientras que en el caso de las funciones, apuntan a una serie de sentencias que realizan una tarea especifica.

#podemos definir funciones para especificar un nombre junto con una secuencia de sentencias que se ejecutan cuando la funcion es "llamada, "ejecutar" o "invocar" 

verses = ["mano hacia el frente", "puño cerrado", "dedo hacia arriba", "lengua afuera"]

def intro():
    print("atencion, compañia")

def chorus():
    print("chuchuwa chu chu wa chuchuwawawa")    
    print("chuchuwa chu chu wa chuchuwawawa") 

def outro():
    print("lalala lalala lalala la la")
    print("lalala lalala lalala la la") 

for verse in verses:
    intro()
    print(verse)
    if verse != verses[-1]:
      chorus()
    else:
      outro()    
    print("-------------")    