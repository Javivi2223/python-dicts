#algunas de las funciones que hemos visto entregan de vuelta su resultado, por ejemplola funcion input() entrega lo escrito por el usuario y luego podemos lo asignar a una variable.

name = input("Dime tu nombre: ")

print(name)

fest = print("Hola mundo")

print(fest)
print("------------")
#las funciones que no retornan nada o que retornan el valor especial **none** se les conoce como funciones void (vacío)

#si queremos que nuestra funcion retorne un valor, lo indicamos con la palabra reservada **return**

def multiply_by_two(number):
  return number * 2

result =multiply_by_two(2)
print(result)      