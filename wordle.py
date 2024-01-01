from os import system
import random
# import requests

# def quitar_tildes(cadena):
#     reemplazos = {
#         'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
#         'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
#     }
#     cadena_sin_tildes = ''.join(reemplazos.get(c, c) for c in cadena)
#     return cadena_sin_tildes

# def palabraExiste(palabra):
#     # url = f'http://dle.rae.es/{palabra.lower()}?m=form'
#     url=f'https://dle.rae.es/srv/search?w={palabra.lower()}'
#     respuesta = requests.get(url)
#     print(url)
#     print (respuesta)
#     if respuesta.status_code == 200:
#         # Analizar la respuesta en formato JSON
#         resultado = respuesta.json()
#         # Extraer la definición si está disponible
#         definiciones = resultado.get('resultados', {}).get('resultados', [])
#         if definiciones:
#             print(definiciones)
#             return 1
#         else:
#             return 0
#     else:
#         return -1



def leerDiccionario():
    archi1=open("diccionario.txt","r")
    linea=archi1.readline()
    diccionario=[]
    while linea!='':
        # print(linea)
        diccionario.append(linea.upper())
        linea=archi1.readline()
    archi1.close()
    return diccionario
def palabradehoy():
    diccionario =leerDiccionario();
    # print(diccionario)
    ret = diccionario[random.randint(0, len(diccionario)) ]
    return ret

def printmy(palabra,resp):
    a_palabra = [char for char in palabra]
    a_resp = [char for char in resp]
    imprimir=''
    for i in range(5):
       
        match a_resp[i]:
            case 'G':
                c="0";
            case 'V':
                c="36";
            case 'A':
                c="33";
            case _:
                c="0"
       
        imprimir=imprimir+  "\033["+c+"m" + a_palabra[i];

    print(imprimir) 

def CalcularRespuesta(palabra,ph):
    ret = ''
   
    a_ph= [char for char in ph]
    a_palabra= [char for char in palabra]
    for i  in range(len(a_ph)-1):
        # print(i)
        if a_ph[i]==a_palabra[i]:
            ret = ret + 'V'
        else:
            letra = 'G'
            for l in ph:
                if a_palabra[i]==l:
                    letra =  'A'
            ret = ret + letra
    
    return ret
def guardarPalabra(palabra,intento,matriz):
    # print(matriz[intento])
    array = [char for char in palabra]
    for i in range(5):
        matriz[intento][i]=array[i]
    return matriz
def inicializarMatriz():
   

    resp = []
    for i in range(6):
        fila =['-','-','-','-','-']
        resp.append(fila)
    return resp
    
def pintarmatriz(palabras,respuestas):
    # system("clear")
    for j in range(len(palabras)):
        f = ''
        r = ''
        for i in range(len(palabras[j])):
            f=f + '' + palabras[j][i]
            r=r + '' + respuestas[j][i]
        
        printmy (f,r)

palabras = inicializarMatriz();
respuestas=inicializarMatriz();
# print(resp);
contador = 0
respuesta = ''
error =''
ph = palabradehoy()
# print(ph)
while (contador<6 and respuesta !="VVVVV"):
    pintarmatriz(palabras,respuestas)
    print(error)
    palabra = input("\033[0m"+"Escribe tu palabra: ")
    palabra=palabra.upper()
    if len(palabra)<5:
       error="\033[31m"+"la palabra tiene que ser de 5 carácteres"
    else:
        # if palabraExiste(palabra)<1:
        #     # error="la palabra no existe"
        # else:
            # palabra= quitar_tildes(palabra)
            error=''
            respuesta = CalcularRespuesta(palabra,ph)
            palabras = guardarPalabra(palabra,contador,palabras);
            respuestas = guardarPalabra(respuesta,contador,respuestas);
            contador= contador +1
    # print(contador)
pintarmatriz(palabras,respuestas)
if respuesta=="VVVVV":
    print("\033[0m"+"¡Enhorabuena!, ¡has ganado!")
else:
    if contador==6:
        print("\033[0m"+
              "oh... lo siento, intentalo de nuevo mañana, la palabra era : " 
            + ph)

