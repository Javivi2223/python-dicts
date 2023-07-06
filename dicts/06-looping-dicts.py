#si utilizamos un loop for para recorrer un diccionario, el for va a recorrer las llaves del diccionario y podemos utilizar las llaves para acceder a los valores.

some_dict = {
  "name": "Javiera",
  "lastname": "Guerrero",
  "weight": 78,
  "height": 1.56  
}

for key in some_dict:
  print(key, some_dict[key])  