#con listas y diccionarios podemos representar estructuras completas similares a lo que encontramos en el mundo real. por ejemplo, podriamos tener un listado de estudiantes
#cada estudiante tiene nombre, apellido, curso  y una lista de sus calificaciones
#ejemplo

students = [
  {
    "name": "Javiera",
    "lastname": "Guerrero",
    "course": "Programación B",
    "grades": [100,90,95,100],
    "active": False
  }, 
     {
    "name": "Lautaro",
    "lastname": "Prieto",
    "course": "Viajes espaciales",
    "grades": [90,100,85,100],
    "active": True
  }
]

#ejercicio manipular arreglos de estudiantes para que muestre la siguiente informacion por cada uno:
#estudiante nombre apellido 
#curso: nombre del curso
#promedio de notas: x
#estado: activo/inactivo

for student in students:
  print("--------------------------")
  print("Estudiante:", student["name"], student["lastname"])
  print("Curso:", student["course"])

  sum = 0
  grades = student["grades"]
  for grade in grades:
    sum += 1
  print("Promedio de notas:", sum/len(grades))

  if student["active"]:
    print("Estado: Activo")
  else:
    print("Estado: Inactivo")  