def PrintIntro(palabra,vidas):
      print("Adivina la palabra secreta de {0} letras".format(len(palabra)))
      print("Tienes {0} vidas para encontrarla".format(vidas))

def PrintPalabra(palabra,letras_dichas,vidas):
      '''
      _ i_ _ a _ a
      '''
      palabra_escondida = ""
      for i in range(len(palabra)):
            for j in range(len(letras_dichas)):
                  if palabra[i] == letras_dichas[j]:
                        palabra_escondida+= letras_dichas[j] +" "
                        break
            else:
                 palabra_escondida+= "_ " 
      
      print("{0:^30}".format(palabra_escondida))
      print("vidas: ",vidas)

def PedirLetra():
      return input("Dame una letra: ")

def LetraDicha(letras_dichas,letra):
      return (letra in letras_dichas)

def Gano(letras_dichas, palabra):
      verificar = 0
      gane = len(palabra)
      for letra_s in palabra:
            for l in letras_dichas:
                  if letra_s == l:
                        verificar+=1
                        break
      return verificar == gane


def Play(palabra,vidas,letras_dichas,letra):
      '''
      Vamos a verificar si la letra, ya fue dicha anteriormente, en el caso de que si, simplemente regresar y no quitar vida mientras tengamos mas de 1 letra guardada
      '''
      if len(letras_dichas)>=1:
            if LetraDicha(letras_dichas, letra):
                  print("La letra {} ya la dijiste".format(letra))
                  return vidas
      letras_dichas.append(letra)

      if not LetraDicha(palabra,letra):
            vidas -=1
            print("No esta la letra '{}' en la palabra ".format(letra))
            return vidas

      else:
            gane = Gano(letras_dichas, palabra)
            if gane:
                  return -1

      return vidas

def EstaVivo(vidas):
      return vidas >0

def OtraPartida(vidas, palabra):
      if vidas == -1: # si gane
            print(" GANASTE!!!!, la palabra secreta fue {}".format(palabra))
      else:
            print("Perdisite! la palabra secreta fue {}".format(palabra))
      seguir = input("Quieres jugar otra vez: ")
      return seguir == "s" or seguir == "S"

from random import randrange
continuar = True 
palabras = ["programacion","uabc","tijuana"]

while continuar:
      palabra = palabras[randrange(len(palabras))] 
      vidas = 3
      letras_dichas = []
      esta_vivo = True
      PrintIntro(palabra,vidas)
      while esta_vivo:
            PrintPalabra(palabra,letras_dichas,vidas)
            letra= PedirLetra()
            vidas= Play(palabra,vidas,letras_dichas,letra)
            esta_vivo = EstaVivo(vidas)
      continuar = OtraPartida(vidas, palabra)
print("Gracias por jugar ...")