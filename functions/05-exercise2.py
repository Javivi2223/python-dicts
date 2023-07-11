#crear triangulo

side_a = int(input("dime el largo del primer lado del triangulo: "))
side_b = int(input("dime el segundo largo del triangulo: "))
side_c = int(input("dime el tercer largo del triangulo: "))
def is_triangle(side1, side2, side3):
  if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print(True)
  else:
    print(False)

is_triangle(side_a, side_b, side_c)    

 