a=4
b=6
c=2
h=10
dmayor=12
dmenor=3
apotema=5
basemayor=20
basemenor=7
radiomayor=6
radiomenor=4
l=8
radio=4.5
n=20
g=7
apotemalateral=9
apotemabase=2
radioesfera=8
radio1=4
radio2=6
pi=3.1416

def cuadrado():
    area=a**2
    perimetro=4*a
    print(f"El area del cuadrado es: {area}")
    print(f"El perimetro del cuadrado es: {perimetro}")

def triangulo():
    area= (b*h)/2
    perimetro=a+b+c
    print(f"El area del triangulo es: {area}")
    print(f"El perimetro del triangulo es: {perimetro}")

def rectangulo():
    area=b*a
    perimetro=2*(b+a)
    print(f"El area del rectangulo es: {area}")
    print(f"El perimetro del rectangulo es: {perimetro}")

def paralelogramo():
    area=b*h
    perimetro=2*(b+a)
    print(f"El area del paralelogramo es: {area}")
    print(f"El perimetro del paralelogramo es: {perimetro}")

def rombo():
    area=(dmayor*dmenor)/2
    perimetro=4*a
    print(f"El area del rombo es: {area}")
    print(f"El perimetro del rombo es: {perimetro}")

def cometa():
    area=(dmayor*dmenor)/2
    perimetro=2*(b+a)
    print(f"El area del cometa es: {area}")
    print(f"El perimetro del cometa es: {perimetro}")

def trapecio():
    area=((basemayor+basemenor)*h)/2
    perimetro=basemayor+basemenor+a+c
    print(f"El area del trapecio es: {area}")
    print(f"El perimetro del trapecio es: {perimetro}")

def circulo():
    area=pi*(radio**2)
    perimetro=2*pi*radio
    print(f"El area del circulo es: {area}")
    print(f"El perimetro del circulo es: {perimetro}")

def poligono_regular():
    perimetro=n*b
    area=(perimetro*a)/2
    print(f"El area del poligono regular es: {area}")
    print(f"El perimetro del poligono regular es: {perimetro}")

def corona_circular():
    area=pi*(radiomayor**2 - radiomenor**2)
    print(f"El area de la corona circular es: {area}")

def sector_circular():
    area=(pi*(radio**2)*n)/360
    print(f"El area del sector circular es: {area}")

def cubo():
    area=6*(a**2)
    volumen=a**3
    print(f"El area del cubo es: {area}")
    print(f"El volumen del cubo es: {volumen}")

def cilindro():
    area=2*pi*radio*(h+radio)
    volumen=pi*(radio**2)*h
    print(f"El area del cilindro es: {area}")
    print(f"El volumen del cilindro es: {volumen}")

def ortoedro():
    area=2*(a*b + a*c + b*c)
    volumen=a*b*c
    print(f"El area del ortoedro es: {area}")
    print(f"El volumen del ortoedro es: {volumen}")

def prisma_recto():
    perimetro=n*l
    areabase=(perimetro*apotema)/2
    area=perimetro*(h+apotema)
    volumen=areabase*h
    print(f"El area del prisma recto es: {area}")
    print(f"El volumen del prisma recto es: {volumen}")

def cono():
    area=pi*radio*(radio+g)
    volumen=(pi*(radio**2)*h)/3
    print(f"El area del cono es: {area}")
    print(f"El volumen del cono es: {volumen}")

def tronco_de_cono():
    area=pi*(g*(radiomenor+radiomayor)+ radiomenor**2 + radiomayor**2)
    volumen=(pi*h*(radiomayor**2 + radiomenor**2 + radiomayor*radiomenor))/3
    print(f"El area del tronco de cono es: {area}")
    print(f"El volumen del tronco de cono es: {volumen}")

def esfera():
    area=4*pi*(radio**2)
    volumen=(4*pi*(radio**3))/3
    print(f"El area de la esfera es: {area}")
    print(f"El volumen de la esfera es: {volumen}")

def piramide():
    areabase=(perimetro*apotemabase)/2
    perimetro=n*l
    area=(perimetro*(apotemabase+apotemalateral))/2
    volumen=(areabase*h)/3
    print(f"El area de la piramide es: {area}")
    print(f"El volumen de la piramide es: {volumen}")

def tetraedro_regular():
    import math
    area=math.sqrt(3)* a**2
    volumen=(math.sqrt(2)* a**3)/12
    print(f"El area del tetraedro regular es: {area}")
    print(f"El volumen del tetraedro regular es: {volumen}")

def octaedro_regular():
    import math
    area=2*math.sqrt(3) * a**2
    volumen=(math.sqrt(2)* a**3)/3
    print(f"El area del octaedro regular es: {area}")
    print(f"El volumen del octaedro regular es: {volumen}")

def tronco_de_piramide():
    import math
    perimetro=n*l
    areabase=(perimetro*apotema)/2
    area=((perimetro*2)/2) * apotema + areabase*2
    volumen=((areabase*2 +math.sqrt(areabase*2))*h)/3
    print(f"El area del tronco de piramide es: {area}")
    print(f"El volumen del tronco de piramide es: {volumen}")

def casquete_esferico():
    area=2*pi*radio*h
    volumen=(pi*h**2*(3*radio-h))/3
    print(f"El area del casquete esferico es: {area}")
    print(f"El volumen del casquete esferico es: {volumen}")

def cuña_esferica():
    area= (4* pi * radio**2 * n)/360
    volumen=(4 * pi * radio**3 * n)/(3*360)
    print(f"El area del huso es: {area}")
    print(f"El volumen del huso es: {volumen}")

def zona_esferica():
    area=2*pi*radioesfera*h
    volumen=(pi*h*(h**2+(3*radio1**2)+(3*radio2**2)))/6
    print(f"El area de la zona esferica es: {area}")
    print(f"El volumen de la zona esferica es: {volumen}")