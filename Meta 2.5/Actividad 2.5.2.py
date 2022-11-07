import math
n=int(input("Ingrese valor de n: "))
def num_triangular(n):
    r=math.sqrt(8*n + 1)
    if (r- int (r) >0):
        return False
    else:
        return True
for i in range(1,n):
    if(num_triangular(i)):
        print(i)
print("Fin")