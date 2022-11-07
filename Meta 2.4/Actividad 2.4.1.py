diccionario = {"a":".-/","b":"-.../","c":"-.-./","d":"-../","e":"./","f":"..-./","g":"--./","h":"..../","i":"../",
"j":".---/","k":"-.-/","l":".-../","m":"--/","n":"-./","o":"---/","p":".--./","q":"--.-/","r":".-./","s":".../","t":"-/",
"u":"..-/","v":"...-/","w":".--/","x":"-..-/","y":"-.--/","z":"--../","1":".----/","2":"..---/","3":"...--/","4":"....-/",
"5":"...../","6":"-..../","7":"--.../","8":"---../","9":"----./","0":"-----/"," ":"/"}
texto=input("Escribe un texto en morse: ")

def morse_a_alfanumerico(texto):
    for caracter in diccionario:
        if diccionario[caracter] == texto:
            return caracter
    return ""

def decodificar_morse(texto):
    texto_alfanumerico = "" 
    for caracter_morse in texto.split(" "):
        # Por cada carácter, buscamos su equivalencia
        caracter_alfanumerico = morse_a_alfanumerico(caracter_morse)
        # Lo concatenamos al resultado.
        texto_alfanumerico += caracter_alfanumerico
    return texto_alfanumerico

traduccion=decodificar_morse(texto)
print(traduccion)