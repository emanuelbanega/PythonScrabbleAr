from pattern.text.es import parse, split, lexicon, spelling
import PySimpleGUI as psg

# aqui empieza lo bueno
def lineal(coor, n):#recibo la lista de coordenadas para verificar si estan en la misma fila o columna,,,
    x = coor[0][n]   #,el parametro n es la cordenada x o y en caso que sea 0 indica la cordenada x y 1 indica la cordenada y
    for i in range(1, len(coor)):#inicio en 1 porque ya tome el primer elemento
        
        if(coor[i][n] != x):
            return False
    return True
    
def esconsecutivo(dicorden,n):#recibo la lista que fue ordenada consecutivamente
    x=int(dicorden[0][0][n])
    for i in range(1,len(dicorden)):
        x=x+1
        if(dicorden[i][0][n]!= x ):
            return False
    "es consecutivo"
    return True


    

def tieneOrden(dic):
    coor=[]
    for c in dic.keys():
        coor.append(c)
   # print("creo una nueva lista con las cordenadas del diccionario\n",coor)
    if(lineal(coor, 0)):#aca mando la lista de coordenadas para ver si tienen la misma fila osea la palabra tiene que ser horizontal
        ordenado1=sorted(dic.items(), key=lambda cor: cor[0][1])#se ordena por columna de menor a mayor
        if (esconsecutivo(ordenado1,1)):
            return ordenado1
    if(lineal(coor, 1)):#aca mando para ver si tienen la misma columna por lo cual la palabra tiene que ser horizontal
        ordenado2= sorted(dic.items(), key=lambda cor: cor[0][0])
        if (esconsecutivo(ordenado2,0)):
            return ordenado2
    return []


def esValida(palabra, *dif):
    palabra = parse(palabra).split('/')
    if palabra[1] in dif:
        if (palabra[1] == 'NN' or palabra[1] == 'NNS' or palabra[1] == 'NNP'):
            if (not palabra[0] in spelling) and (not palabra[0] in lexicon):
                return False
        #print('existe'+ palabra[1])
        return True
    return False

def formarPalabra(lista):
    #buscar si se puede evitar el orden post lambda siguiente ordenando una lista de 
    # valores en base a las claves del diccionario <-----------------------------------
    s=''
    for i in range(len(lista)):
        s+=lista[i][1]
    return s

def validez(dif,coor,letras):
    aux={}
    for i in range(len(coor)):#guardo las cordenadas como clave y las letras como su valor
        aux[coor[i]]=letras[i]
    #verifico si todas las letras estan en una fila/columna y las ordeno
    aux = tieneOrden(aux.copy())
    if aux==[]:
        psg.popup('No posee orden')
        return 0
    #armo la palabra con las letras ordenadas
    palabra = formarPalabra(aux)##################################################################################################
    palabra = palabra.lower()
    
    #verifico si la palabra existe
    #palabra=input()
    if(esValida(palabra, *dif)):
        psg.popup('Bien!')
        return 2
    else:
        psg.popup('NoEsCorrecta')
        return 1
