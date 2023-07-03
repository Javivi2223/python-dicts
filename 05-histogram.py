#un histogram de frecuencia sirve para representar cuantas veces aparece cierto elemento en una coleccion o mas en general sirve para resumir resultados.
#supongamos que nos dan una palabra y necesitamos contar cuantas veces aparece cada letra en la palabra

word = input("Dime una palabra: ")

letter_counter = {}

for letter in word:
  if letter in letter_counter:
    letter_counter[letter] += 1
  else:
    letter_counter[letter] = 1

print(letter_counter)      
