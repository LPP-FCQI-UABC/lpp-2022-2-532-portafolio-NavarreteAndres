#cuadrado
I=int(input("ingrese el valor del lado: "))
area=I**2
print(f"el area es: {area}")

#triangulo
base=int(input("Ingrese la base: "))
altura=int(input("ingrese la altura"))
area=int(base)*int(altura)/2
print("el area es: {area}")

#rectangulo
base=int(input("Ingrese la base: "))
altura=int(input("ingrese la altura"))
area=int(base)*int(altura)
print("el area es: {area}")

#rombo
D=int(input("ingrese el diametro mayor: "))
d=int(input("ingrese el diametro menor: "))
area=int(D)*int(d)/2
print("el area es: ")

#trapecio
B=int(input("ingrese la base mayor: "))
b=int(input("ingrese la base menor: "))
altura=int(input("ingrese la altura"))
area=int((B+b)*altura)/2
print("el area es: {area}")

#circulo
pi=3.1416
d=int(input("ingrese el diametro: "))
area=int(pi*d)
print("el area es: {area}")

#poligono regular
n=int(input("ingrese numero de lados: "))
b=int(input("ingrese medida de un lado: "))
perimetro=int(n*b)
print("el perimetro es: {perimetro}")
a=int(input("ingrese el apotema: "))
area=int(perimetro*a)/2
print("el area es: {area}")

