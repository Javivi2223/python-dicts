from time import sleep
#en el contexto de la programacion las funciones son una secuencia de sentencias de codigo con un nombre.
#se parecen en algo a las variables en el sentido que son un simple nombre. en el caso de las variables, estas apuntan a un valor, mientras que en el caso de las funciones, apuntan a una serie de sentencias que realizan una tarea especifica.

#python trae varias funciones ya listas con las clasicas print(), int(), len(), etc.

#podemos definir funciones para especificar un nombre junto con una secuencia de sentencias que se ejecutan cuando la funcion es "llamada", "ejecutada" o "invocada" 

#algunas funciones pueden requerir argumentos. por ejemplo print() recibe como argumento lo que va a imprimir en la termina. algunas funciones reciben mas de un argumento.

# un detalle es que cuando estamos dentro de la funcion los argumentos se asignan a variables locales llamadas **parametros**. profundizaremos esto mas adelante

verses = ["mano hacia el frente", "puño cerrado", "dedo hacia arriba", "lengua afuera"]

def intro(verse):
    print(f"atencion, compañia!: {verse}")
    sleep(1)

def chorus():
    print("chuchuwa") 
    sleep(1)   
    print("chuchuwa")
    sleep(1) 
    print("chuchuwa wa wa")
    sleep(0.5)
   
def outro():
    print("lalala lalala lalala la la")
    print("lalala lalala lalala la la") 

for verse in verses:
    intro(verse)
    #esto revisa si el verso NO es el ultimo de los versos
    if verse != verses[-1]:
      chorus()
    else:
      outro()    
    print("-------------")    