from math import sqrt
#crear una función que retone la hipotenusa en un rectangulo

def hyp(side1,side2):
  return sqrt(side1**2 + side2**2)     

result = hyp(3,4) 

print(f"el resultado de la hipotenusa es {result}")
